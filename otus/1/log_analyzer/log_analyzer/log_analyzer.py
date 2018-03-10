#!/usr/bin/env python
# -*- coding: utf-8 -*-


# log_format ui_short '$remote_addr $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';
import argparse
import datetime
import json
import os
import re
import sys

config = {
    "REPORT_SIZE": 1000,
    "REPORT_DIR": "./reports",
    "LOG_DIR": "./log"
}


def load_config(path_to_file: str) -> dict:
    """
    Возвращает конфиг считывая его из файла
    :param path_to_file:
    :return:
    """
    try:
        with open(path_to_file, 'rb') as config_file:
            try:
                config = json.loads(config_file.read())
            except json.JSONDecodeError as e:
                sys.exit(f"Broken configuration file: {path_to_file}")
    except FileNotFoundError as e:
        sys.exit(f"{e.strerror}: {path_to_file}")

    return config


def get_last_log_file(path_to_log_dir):
    """
    Возвращает путь к самому свежему файлу лога из переданной директории path_to_log_dir, фильтрует
    файлы согласно паттерну ниже.
    :param path_to_log_dir:
    :return:
    """
    pattern = r"nginx-access-ui.log-(?P<date>\d{8})(.gz)?"
    files_dict = {}
    for f in os.listdir(path_to_log_dir):
        match = re.match(pattern, f)
        date_group = match.group(1)
        if match:
            files_dict[datetime.datetime.strptime(date_group, "%Y%m%d").date()] = os.path.join(path_to_log_dir, f)
    date_list = list(files_dict.keys())
    date_list.sort()

    return files_dict[date_list[-1]]


def main(config: dict, args):
    loaded_config = load_config(args.config)
    merged_config = {**config, **loaded_config}
    log_file = get_last_log_file(merged_config['LOG_DIR'])



    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log analyzer')

    parser.add_argument('--config', type=str, default='config.json', help='path to configuration file')
    args = parser.parse_args('')

    main(config, args)

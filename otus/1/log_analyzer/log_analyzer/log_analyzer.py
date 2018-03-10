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
from string import Template

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
                loaded_config = json.loads(config_file.read())
            except json.JSONDecodeError as e:
                sys.exit(f"Broken configuration file: {path_to_file}")
    except FileNotFoundError as e:
        sys.exit(f"{e.strerror}: {path_to_file}")

    return loaded_config


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
            try:
                files_dict[datetime.datetime.strptime(date_group, "%Y%m%d").date()] = os.path.join(path_to_log_dir, f)
            except ValueError as e:
                sys.exit(f"Incorrect date format in name of file '{f}', it must be %Y%m%d")

    date_list = list(files_dict.keys())
    date_list.sort()

    return files_dict[date_list[-1]]


def render(table_json: str, report_name: str, report_dir: str, path_to_template="./templates/report.html"):
    try:
        with open(path_to_template, "r") as f_out:
            html_template = f_out.read()

            if not os.path.exists(report_dir):
                os.makedirs(report_dir)

            path_to_report_file = os.path.join(report_dir, report_name)
            try:
                with open(path_to_report_file, "w") as f_in:
                    f_in.write(Template(html_template).safe_substitute(table_json=table_json))
            except FileNotFoundError as e:
                sys.exit(f"Wrong path to report file: {path_to_report_file} ({e.strerror})")
    except FileNotFoundError as e:
        sys.exit(f"Wrong path to template: {path_to_template} ({e.strerror})")


def calculate_report(path_to_log_file, size=1000):
    table = dict()
    with open(path_to_log_file, "r") as f_out:
        own_num_rows = 0  # общее количество строк в логе
        error_rows = 0  # количество нераспарсенных строк
        own_num_request = 0  # общее количество распарсенных запросов
        own_sum_request_time = 0  # $request_time всех запросов
        for line in f_out:
            own_num_rows += 1
            match = re.search(r"(?P<path>\S+) HTTP\/1\.\d\".*\"(?P<request_time>.*)", line)
            if match:
                own_num_request += 1
                path = match.group(1)
                request_time = match.group(2)
                request_time = float(request_time.strip())
                own_sum_request_time += request_time

                if path in table:
                    table[path]['count'] += 1
                    table[path]['time_sum'] += request_time
                    table[path]['time_avg'].append(request_time)
                    table[path]['time_max'] = request_time if request_time > table[path]['time_max'] else table[path]['time_max']
                else:
                    table[path] = {'url': path,
                                   'count': 1,
                                   'count_perc': 0,
                                   'time_avg': [request_time],
                                   'time_max': request_time,
                                   'time_med': 0,
                                   'time_perc': 0,
                                   'time_sum': request_time}
            else:
                error_rows += 1
    table = list(table.values())
    table.sort(key=lambda el: el['time_sum'], reverse=True)
    table = table[0:size]

    for row in table:
        row['time_avg'] = sum(row['time_avg']) / len(row['time_avg'])
        row['count_perc'] = row['count'] * 100 / own_num_request
        row['time_perc'] = row['time_sum'] * 100 / own_sum_request_time
    return table


def main(config: dict, args):

    loaded_config = load_config(args.config)
    merged_config = {**config, **loaded_config}

    path_to_log_dir = os.path.abspath(merged_config['LOG_DIR'])
    log_file = get_last_log_file(path_to_log_dir)

    calculate_report(log_file, size=merged_config['REPORT_SIZE'])
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log analyzer')
    parser.add_argument('--config', type=str, default='config.json', help='path to configuration file')
    args = parser.parse_args()

    main(config, args)

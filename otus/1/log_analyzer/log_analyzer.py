#!/usr/bin/env python
# -*- coding: utf-8 -*-


# log_format ui_short '$remote_addr $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';
import argparse

config = {
    "REPORT_SIZE": 1000,
    "REPORT_DIR": "./reports",
    "LOG_DIR": "./log"
}


def main(config):

    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log analyzer')

    parser.add_argument('--config', type=str, help='path to configuration file')
    args = parser.parse_args()
    main(config)

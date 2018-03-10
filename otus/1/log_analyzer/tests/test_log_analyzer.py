import gzip
import json
import shutil
import unittest

import os
from log_analyzer.log_analyzer import load_config, get_last_log_file


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        super(TestLogAnalyzer, self).setUp()

        self.abs_path = os.getcwd()
        self.path_to_temp = os.path.join(self.abs_path, 'tests', 'temp')

        if os.path.exists(self.path_to_temp):
            shutil.rmtree(self.path_to_temp)

        os.makedirs(self.path_to_temp)

    def tearDown(self):
        shutil.rmtree(self.path_to_temp)

    def _generate_plain_sample(self, file_name="nginx-access-ui.log-20170630"):
        content = """1.196.116.32 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/25019354 HTTP/1.1" 200 927 "-" "Lynx/2.8.8dev.9 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/2.10.5" "-" "1498697422-2190034393-4708-9752759" "dc7161be3" 0.390
1.99.174.176 3b81f63526fa8  - [29/Jun/2017:03:50:22 +0300] "GET /api/1/photogenic_banners/list/?server_name=WIN7RB4 HTTP/1.1" 200 12 "-" "Python-urllib/2.7" "-" "1498697422-32900793-4708-9752770" "-" 0.133
1.169.137.128 -  - [29/Jun/2017:03:50:22 +0300] "GET /api/v2/banner/16852664 HTTP/1.1" 200 19415 "-" "Slotovod" "-" "1498697422-2118016444-4708-9752769" "712e90144abee9" 0.199
        """
        path_to_file = os.path.join(self.path_to_temp, file_name)
        with open(path_to_file, "w") as file:
            file.write(content)

        return path_to_file

    def _generate_gz_sample(self, file_name="nginx-access-ui.log-20170630", is_remove_plain=False):
        path_to_plain_file = self._generate_plain_sample(file_name)
        patrh_to_gz_file = f'{path_to_plain_file}.gz'

        with open(path_to_plain_file, 'rb') as f_in:
            with gzip.open(patrh_to_gz_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        if is_remove_plain:
            os.remove(path_to_plain_file)

        return patrh_to_gz_file

    def _generate_config_file(self, file_name="config.json", config=None):

        if config is None:
            config = {
                "REPORT_SIZE": 1000,
                "REPORT_DIR": "./reports",
                "LOG_DIR": "./log"
            }
        path_to_config_file = os.path.join(self.path_to_temp, file_name)

        with open(path_to_config_file, 'w') as f_out:
            f_out.write(json.dumps(config))

        return path_to_config_file

    def test_load_normal_config(self):
        path_to_config_file = self._generate_config_file()

        config = load_config(path_to_config_file)
        self.assertIsInstance(config, dict)

    def test_load_does_not_exist_config(self):
        with self.assertRaises(SystemExit) as exc:
            load_config("some_wrong_path_to_config.json")
        self.assertIsInstance(exc.exception, SystemExit)

    def test_load_broken_json_config(self):
        path_to_config_file = self._generate_config_file(config="wrong config")
        with open(path_to_config_file, 'w') as f_out:
            f_out.write("some text, which broke json-format")

        with self.assertRaises(SystemExit) as exc:
            load_config(path_to_config_file)
        self.assertIsInstance(exc.exception, SystemExit)

    def test_validation_loaded_config(self):
        path_to_config_file = self._generate_config_file()
        config = load_config(path_to_config_file)

        self.assertTrue("REPORT_SIZE" in config)
        self.assertTrue("REPORT_DIR" in config)
        self.assertTrue("LOG_DIR" in config)
        self.assertEqual(len(config), 3)

    def test_take_last_log_file_plain(self):
        template = "nginx-access-ui.log-201706"
        log_name_list = [f"{template}{str(day).zfill(2)}" for day in range(1, 4)]
        log_file_path_list = [self._generate_plain_sample(log_name) for log_name in log_name_list]

        path_to_last_log_file = get_last_log_file(self.path_to_temp)
        self.assertTrue(path_to_last_log_file in log_file_path_list)
        self.assertEqual(path_to_last_log_file, log_file_path_list[-1])

    def test_take_last_log_file_gz(self):
        template = "nginx-access-ui.log-201706"
        log_name_list = [f"{template}{str(day).zfill(2)}" for day in range(1, 4)]
        log_file_path_list = [self._generate_gz_sample(log_name, is_remove_plain=True) for log_name in log_name_list]

        path_to_last_log_file = get_last_log_file(self.path_to_temp)
        self.assertTrue(path_to_last_log_file in log_file_path_list)
        self.assertEqual(path_to_last_log_file, log_file_path_list[-1])

    def test_take_last_log_file_gz_and_plain_mixed(self):
        template = "nginx-access-ui.log-201706"
        log_name_list = [f"{template}{str(day).zfill(2)}" for day in range(1, 4)]
        gz_list = [self._generate_gz_sample(log_name, is_remove_plain=True) for log_name in log_name_list]

        log_name_list = [f"{template}{str(day).zfill(2)}" for day in range(4, 6)]
        plain_list = [self._generate_plain_sample(log_name) for log_name in log_name_list]

        path_to_last_log_file = get_last_log_file(self.path_to_temp)
        self.assertTrue(path_to_last_log_file in plain_list)
        self.assertTrue(path_to_last_log_file not in gz_list)
        self.assertEqual(path_to_last_log_file, plain_list[-1])

    def test_take_last_log_wrong_format_date(self):
        self._generate_plain_sample("nginx-access-ui.log-01052017")

        with self.assertRaises(SystemExit) as exc:
            get_last_log_file(self.path_to_temp)
        self.assertIsInstance(exc.exception, SystemExit)

    def test_processing_not_exist_log(self):
        pass

    def test_repeat_processing_the_same_log(self):
        pass


if __name__ == '__main__':
    unittest.main()

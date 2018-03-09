import gzip
import shutil
import unittest

import os


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

    def _generate_gz_sample(self, file_name="nginx-access-ui.log-20170630"):
        path_to_plain_file = self._generate_plain_sample(file_name)
        patrh_to_gz_file = f'{path_to_plain_file}.gz'

        with open(path_to_plain_file, 'rb') as f_in:
            with gzip.open(patrh_to_gz_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    def test_take_last_log_file_plain(self):
        template = "nginx-access-ui.log-201706"
        log_name_list = [f"{template}{str(day).zfill(2)}"for day in range(1,4)]

        log_file_path_list = [self._generate_plain_sample(log_name) for log_name in log_name_list]


    def test_take_last_log_file_gz(self):
        pass

    def test_take_last_log_file_gz_and_plain(self):
        pass

    def test_processing_not_exist_log(self):
        pass

    def test_repeat_processing_the_same_log(self):
        pass


if __name__ == '__main__':
    unittest.main()

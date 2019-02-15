import unittest
import requests
from lib.read_excel import *
import json
from config.config import *
from lib.case_log import log_case_info  # 导入方法

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_login_normal')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url, data=json.loads(data))
        log_case_info('test_user_login_normal', url, data, expect_res, res_text)  # 输出用例log信息
        self.assertEqual(res.text, expect_res)

if __name__ == '__main__':
    unittest.main(verbosity=2)
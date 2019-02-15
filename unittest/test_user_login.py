import unittest
import requests


class TestUserLogin(unittest.TestCase):
    url = "http://10.1.1.71:9999/syscenter/api/v1/currentUser"


    def test_user_login_nomal(self):
        data = {"name":"wangmm","password":"e10adc3949ba59abbe56e057f20f883e"}
        res = requests.post(url=self.url,data = data)
        print(res.text)
        # self.assertIn("王萌萌",res.text)



if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main(verbosity=2)

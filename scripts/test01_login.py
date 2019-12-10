import unittest

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 获取Apilogin对象
        cls.login = ApiLogin()
    # 登录测试方法
    def test01_login(self,mobile="13800000002",password="123456"):
        # 调用业务方法
        r = self.login.api_login(mobile,password)

        token = r.json().get("data")
        api.headers['Authorization'] = "Bearer " + token

        print("登录成功后headers值位",api.headers)
        # 断言
        assert_common(self,r)


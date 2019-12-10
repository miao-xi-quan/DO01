import unittest
import requests
from parameterized import parameterized

import api
from api.api_employee import ApiEmployee
from scripts.read_txt import read_txt

from tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取ApliEmployee对象
        cls.api = ApiEmployee()

    # 新增员工
    @parameterized.expand(read_txt("employee_post.txt"))
    def test01_post(self,username="miao1234",mobile="12234611441",workNumber="888888"):
        # 调用新增接口
        r = self.api.api_post_employee(username,mobile,workNumber)
        print("新增员工后结果:",r.json())
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        print("新增员工id为:",api.user_id)
        # 断言
        assert_common(self,r)

    # 更新数据
    def test02_put(self,username="xi1234"):
        r = self.api.api_put_employee(username)
        print("更新数据为:",r.json())
        assert_common(self,r)

    # 查看数据
    def test03_get(self):
        r = self.api.api_get_employee()
        print("查看员工名称:",r.json())
        assert_common(self,r)


    # 删除
    def test04_delete(self):
        # 调用删除接口
        r = self.api.api_delete_employee(api.user_id)
        print("删除数据结果为:",r.json())
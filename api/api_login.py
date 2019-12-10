import api
import requests

class ApiLogin:
    # 初始化
    def __init__(self):
        # 初始化url
        self.url = api.BASE_URL + "/api/sys/login"

    # 登录
    def api_login(self,mobile,pasword):
        # 定义请求json串
        data = {"mobile":mobile,"password":pasword}

        return requests.post(url=self.url,json=data,headers=api.headers)


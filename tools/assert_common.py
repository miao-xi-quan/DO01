

def assert_common(self,response,status_code=200,msg="操作成功！"):
    # 断言状态码200
    self.assertEqual(status_code, response.status_code)
    # 断言success
    self.assertTrue(response.json().get("success"))
    # 断言code
    self.assertEqual(10000,response.json().get("code"))
    # 断言message
    self.assertEqual(msg, response.json().get("message"))
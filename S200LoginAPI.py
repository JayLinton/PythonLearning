import pytest
from http.client import responses

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 抑制警告


@pytest.fixture()
def login_info():
    username = "admin"  # 必填，系统登录账号
    password = "HuaWei123"  # 必填，系统登录密码
    ip = "90.66.46.120"
    port = "18532"
    return username, password, ip, port


class TestLogin:

    def setup_class(self):
        print('测试类准备')

    def teardown_class(self):
        print('测试类清理')

    def setup_method(self):
        print('测试方法准备')

    def teardown_method(self):
        print('测试方法清理')

    # def __init__(self, ip, port):  # 初始化ip和端口号
    #     self.ip = "90.66.46.120"
    #     self.port = "18532"
    #     self.userName = 'admin'
    #     self.password = 'HuaWei123'

    def test_login(self, login_info):
        # 请求地址（根据实际服务器地址修改）
        url = f"https://{login_info[2]}:{login_info[3]}/api/HttpGetWei/loginInfo/login/v1.0"

        # 请求头
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }

        # 请求参数（替换为实际账号密码）
        data = {
            "userName": login_info[0],  # 必填，系统登录账号
            "password": login_info[1]  # 必填，系统登录密码
        }

        try:
            # 发送POST请求
            response = requests.post(
                url=url,
                headers=headers,
                json=data,  # 自动将字典转换为JSON格式
                verify=False  # 跳过SSL证书验证（测试环境使用）
            )

            # 检查HTTP状态码
            if response.status_code != 200:
                print(f"HTTP请求失败，状态码：{response.status_code}")
                return

            # 解析响应内容
            result = response.json()
            print("完整响应内容：", json.dumps(result, ensure_ascii=False, indent=2))

            # 判断业务结果
            assert result.get("resultCode") == 0, f"登录失败，错误码：{result.get('resultCode')}"

        except requests.exceptions.RequestException as e:
            print("请求发生异常：", e)
        except json.JSONDecodeError:
            print("响应内容无法解析为JSON格式")


if __name__ == '__main__':
    pytest.main(['-v', __file__])

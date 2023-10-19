"""
学习接口自动化测试的第一次: requests模块

"""
import os
import re

import pytest
import requests


class TestSendRequest:
    access_token = ""
    csrf_token = ""
    cks = ""   # 由于使用get_session()得到session后,就不需要使用cookie,所以注释掉了！

    # 讲到接口自动化测试框架封装引入的方法:
    # session = requests.session()

    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }
        # 发送get请求: Ctrl+左键查看函数(方法)的api文档
        rep = requests.get(url=url, params=data)
        # rep = requests.request("get", url=url, params=data)
        # rep = self.session.request("get", url=url, params=data)

        print(f"发送get请求后,接收的rep的类型是: {type(rep)}, 数据是: {rep}")
        # .json()方法是requests库中的一个方法，用于解析HTTP响应对象的内容，
        # 将JSON数据从字符串形式转换为Python数据结构，通常是字典或列表。
        get_data = rep.json()
        print(f"get_data的类型是: {type(get_data)},数据是: \n{get_data}")

        # 从返回值中提取token值
        TestSendRequest.access_token = get_data['access_token']
        print(TestSendRequest.access_token)

    def test_edit_flag(self):
        # # 通过之前写入到extract.yaml文件中的access_token值进行读取
        # value = TokenYmlUtil().read_extract_yaml('access_token')
        # # print(value)
        # url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=ACCESS_TOKEN"
        # url = f"https://api.weixin.qq.com/cgi-bin/tags/update?access_token={self.access_token}"
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + TestSendRequest.access_token + ""
        data = {
            "tag": {"id": 134, "name": "福建人"}
        }
        # 发送post请求(从post的文档中可以知道: data和json只需要传一个,它们有什么区别?)
        """
        json: 不管是dict还是str类型,默认都是application/json,格式: {"a":1,"b":"2"}
        data: 
              (1)dict字典类型,那么默认情况下请求头: application/x-www-form-urlencoded,
              表示以form表单的方式传参,格式: a=1&b=2&c=3
              (2)str类型,那么默认情况下: text/plain(如果是字典格式需要转换成str格式传参)
        这里涉及:
              json.dumps(data): 把字典格式的数据转换成str格式
              json.loads(data): 把str格式转换成字典格式
        总结: 
            data只能传简单的只有键值对的dict或者str格式。json一般只能传dict格式(简单和嵌套都可以)
        """
        rep = requests.post(url, json=data)
        # rep = requests.request("post", url, json=data)
        # rep = self.session.request("post", url, json=data)

        # print(f"发送post请求后,返回的rep的类型是: {type(rep)}, 数据是: {rep}")
        rep_data = rep.json()
        print(f"返回的响应rep_data的类型是: {type(rep_data)}, 数据是: \n{rep_data}")

    def test_file_upload(self):
        # url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=ACCESS_TOKEN"
        url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={TestSendRequest.access_token}"
        data = {
            "media": open(r"D:\xiaoma.png", "rb")
        }
        rep = requests.post(url=url, files=data)
        # rep = requests.request("post", url=url, files=data)
        # rep = self.session.request("post", url=url, files=data)

        print(f"上传文件后,返回值rep.json(): {rep.json()}")

    def test_start(self):
        url = "http://47.107.116.139/phpwind/"

        rep = requests.get(url=url)
        # # rep = requests.request("get", url=url)
        # rep = self.session.request("get", url=url)

        # print(f"发送get请求后,接收的rep的类型是: {type(rep)}, 数据是: {rep}")
        # print(rep.text)
        # 通过正则表达式获取token鉴权码
        TestSendRequest.csrf_token = re.search('name="csrf_token" value="(.*?)"', rep.text)[1]
        print(TestSendRequest.csrf_token)

        # 这一步是给下面登录测试用例test_login获取cookie值用的
        # 但是,后续是使用了get_session()方法获取cookie的话,就可以不用这里再去获取cookies了
        TestSendRequest.cks = rep.cookies

    # 请求需要带请求头的接口
    def test_login(self):

        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username": "msxy",
            "password": "msxy",
            "csrf_token": TestSendRequest.csrf_token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        # 注意: 这步就是添加请求头,如果没有这部分的话,必须用print(login_rep.text),因为返回的是网页
        # 添加下面内容后,用print(rep.json()),返回的json格式的数据
        headers = {
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }

        # 添加完上面的请求头后,运行后发现"state"是"fail",原因是没有做cookie的鉴权
        # cookie鉴权: 网页的接口基本上都要做cookie的鉴权,
        # 所以,需要在上一步骤的test_start中先去获取到cookie值
        # 但是后面再通过get_session()方法后,就通过session,就不需要cookie了
        rep = requests.post(url=url, data=data, headers=headers, cookies=TestSendRequest.cks)
        # rep = requests.request("post", url=url, data=data, headers=headers, cookies=TestSendRequest.cks)
        # rep = self.session.request("post", url=url, data=data, headers=headers)

        print(rep.json())


if __name__ == '__main__':
    pytest.main(['-vs'])
    # pytest.main(['-vs', '--html=./report.html'])

# pytest -vs --alluredir=D:/以前の資料/workspace/pythonwork/publicdemo/venv/reports --allure-severities normal

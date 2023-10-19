"""
学习接口自动化测试的第一次: requests模块

"""
import os
import re

import pytest
import requests

from publicdemo.common.token_yaml_util import TokenYmlUtil


class TestSendRequest:
    # 讲到接口自动化测试框架封装引入的方法:
    session = requests.session()

    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }
        # 发送get请求: Ctrl+左键查看函数(方法)的api文档
        # rep = requests.get(url=url, params=data)
        # rep = requests.request("get", url=url, params=data)
        rep = self.session.request("get", url=url, params=data)
        print(f"通过rep.json()获取到的返回值是: {rep.json()}")

        # 将access_token的值通过common目录下的token_yaml_util.py类文件下的read_extract_yaml方法写入到extract.yaml文件里
        TokenYmlUtil().write_extract_yaml({'access_token': rep.json()['access_token']})

        # 通过断言,如果结果不在预期值里,就会报错,这样避免通过肉眼去看输出值(或打印信息)来判别代码是否达到预期目的
        assert 'access_token' in rep.json()

    def test_edit_flag(self):
        # 读取之前写入到extract.yaml文件中的access_token值
        access_token = TokenYmlUtil().read_extract_yaml('access_token')

        # url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=ACCESS_TOKEN"
        # url = f"https://api.weixin.qq.com/cgi-bin/tags/update?access_token={self.access_token}"
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + access_token + ""
        data = {
            "tag": {"id": 134, "name": "福建人"}
        }

        # rep = requests.post(url, json=data)
        # rep = requests.request("post", url, json=data)
        rep = self.session.request("post", url, json=data)

        # print(f"发送post请求后,返回的rep的类型是: {type(rep)}, 数据是: {rep}")
        rep_data = rep.json()
        print(f"返回rep.json()的类型是: {type(rep_data)}, 数据是: \n{rep_data}")

        # 通过rep.json()返回值进行断言: {'errcode': 0, 'errmsg': 'ok'}
        assert rep_data['errcode'] == 0

    def test_file_upload(self):
        access_token = TokenYmlUtil().read_extract_yaml('access_token')
        # url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=ACCESS_TOKEN"
        url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={access_token}"
        data = {
            "media": open(r"D:\xiaoma.png", "rb")
        }
        # rep = requests.post(url=url, files=data)
        # rep = requests.request("post", url=url, files=data)
        rep = self.session.request("post", url=url, files=data)

        print(f"上传文件后,返回值rep.json()是: {rep.json()}")
        # 通过返回值rep.json()中是否有url值来进行断言
        assert 'url' in rep.json()

    def test_start(self):
        url = "http://47.107.116.139/phpwind/"

        # rep = requests.get(url=url)
        # # rep = requests.request("get", url=url)
        rep = self.session.request("get", url=url)

        # print(f"发送get请求后,接收的rep的类型是: {type(rep)}, 数据是: {rep}")
        # print(rep.text)
        # 通过正则表达式获取csrf_token鉴权码
        # TestSendRequest.csrf_token = re.search('name="csrf_token" value="(.*?)"', rep.text)[1]
        # print(TestSendRequest.csrf_token)

        # 这一步是给下面登录测试用例test_login获取cookie值用的
        # 但是,后续是使用了get_session()方法获取cookie的话,就可以不用这里再去获取cookies了
        # TestSendRequest.cks = rep.cookies

        # 通过正则表达式将获取到csrf_token的值写入到extract.yml文件中
        TokenYmlUtil().write_extract_yaml({'csrf_token': re.search('name="csrf_token" value="(.*?)"', rep.text)[1]})

    # 请求需要带请求头的接口
    def test_login(self):
        csrf_token = TokenYmlUtil().read_extract_yaml('csrf_token')
        # # 从extract.yml文件获取之前写入的csrf_token值
        # csrf_token = TokenYmlUtil().read_extract_yaml('csrf_token')
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username": "msxy",
            "password": "msxy",
            "csrf_token": csrf_token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        # 注意: 这步就是添加请求头, 其实就是客户端告诉服务端返回的是json格式的报文。
        # 如果没有这部分的话,必须用print(login_rep.text),因为返回的是网页
        # 添加下面内容后,用print(rep.json()),就能返回json格式的数据,否则print(rep.json())会报错。
        headers = {
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }

        # 添加完上面的请求头后,运行后发现"state"是"fail",原因是没有做cookie的鉴权
        # cookie鉴权: 网页的接口基本上都要做cookie的鉴权,
        # 所以,需要在上一步骤的test_start中先去获取到cookie值
        # 但是后面再通过get_session()方法后,就通过session,就不需要cookie了
        # rep = requests.post(url=url, data=data, headers=headers, cookies=TestSendRequest.cks)
        # rep = requests.request("post", url=url, data=data, headers=headers, cookies=TestSendRequest.cks)
        rep = self.session.request("post", url=url, data=data, headers=headers)

        print(rep.json())

        # assert rep.json()['state'] == 'success'


if __name__ == '__main__':
    pytest.main(['-vs'])
    # pytest.main(['-vs', '--html=./report.html'])

# pytest -vs --alluredir=D:/以前の資料/workspace/pythonwork/publicdemo/venv/reports --allure-severities normal

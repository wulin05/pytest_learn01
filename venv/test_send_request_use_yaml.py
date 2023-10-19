"""
学习接口自动化测试,配合使用yaml文件的读取、写入操作

"""
import json
import os
import re
import pytest
import requests

from publicdemo.common.requests_util import RequestUtil
from publicdemo.common.token_yaml_util import TokenYmlUtil


class TestSendRequest:
    # 讲到接口自动化测试框架封装引入的方法:
    # session = requests.session()

    @pytest.mark.parametrize("caseinfo", TokenYmlUtil().read_yaml_contents('/venv/yaml_data/get_token.yaml'))
    def test_get_token(self, caseinfo):
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']

        rep = RequestUtil().send_request(method, url, data=data)
        rep_data = rep.json()
        # print(f"rep.json的类型是: {type(rep_data)}, 返回值是: {rep_data}")
        if 'access_token' in rep_data:
            TokenYmlUtil().write_extract_yaml({'access_token': rep_data['access_token']})
        else:
            assert rep_data['errcode'] == 45009

    @pytest.mark.parametrize("caseinfo", TokenYmlUtil().read_yaml_contents('/venv/yaml_data/edit_flag.yaml'))
    def test_edit_flag(self, caseinfo):
        # 读取之前写入到extract.yaml文件中的access_token值
        access_token = TokenYmlUtil().read_extract_yaml('access_token')

        method = caseinfo['request']['method']
        # url = caseinfo['request']['url']+"?access_token="+access_token+""
        url = caseinfo['request']['url'] + "?access_token=" + f"{access_token}"
        data = caseinfo['request']['data']

        # rep = RequestUtil().send_request(method, url, data=json.dumps(data))
        RequestUtil().send_request(method, url, data=json.dumps(data))
        # rep = self.session.request(method, url, json=data)
        # print(f"发送post请求后,返回的rep的类型是: {type(rep)}, 数据是: {rep}")

        # rep_data = rep.json()
        # print(f"返回rep.json()的类型是: {type(rep_data)}, 数据是: \n{rep_data}")
        #
        # # 针对edit_flag.yaml文件的正常、错误的数据进行异常处理
        # assert rep_data['errcode'] == 0

    # @pytest.mark.parametrize('caseinfo', TokenYmlUtil().read_yaml_contents('yaml_data/file_upload.yaml'))
    # 目前学到的,yaml文件不支持open参数(老师说,有其他的方式可以通过yaml文件实现文件的上传)
    # 所以根本不能使用TokenYmlUtil().read_yaml_contents('yaml_data/file_upload.yaml')来实现上传文件。
    def test_file_upload(self):
        # session = requests.session()
        access_token = TokenYmlUtil().read_extract_yaml('access_token')
        # url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=ACCESS_TOKEN"
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + access_token + ""
        files = {
            "media": open(r"D:\xiaoma.png", "rb")
        }

        # rep = requests.post(url=url, files=files)
        # rep = RequestUtil().send_request(method="post", url=url, data=None, files=files)
        RequestUtil().send_request(method="post", url=url, data=None, files=files)
        # rep = session.request("post", url=url, files=data)

        # print(f"上传文件后,返回值rep.json()是: {rep.json()}")
        # 通过返回值rep.json()中是否有url值来进行断言
        # assert 'url' in rep.json()

    @pytest.mark.parametrize("caseinfo", TokenYmlUtil().read_yaml_contents('/venv/yaml_data/start.yaml'))
    def test_start(self, caseinfo):
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']

        rep = RequestUtil().send_request(method, url, data=None)
        # rep = self.session.request(method, url=url)
        # print(f"发送get请求后,接收的rep的类型是: {type(rep)}, 数据是: {rep}")
        # print(rep.text)
        # 通过正则表达式获取csrf_token鉴权码
        # TestSendRequest.csrf_token = re.search('name="csrf_token" value="(.*?)"', rep.text)[1]
        # print(TestSendRequest.csrf_token)

        # 这一步是给下面登录测试用例test_login获取cookie值用的
        # 但是,后续是使用了get_session()方法获取cookie的话,就可以不用这里再去获取cookies了
        # TestSendRequest.cks = rep.cookies

        # 通过正则表达式将获取到csrf_token的值写入到extract.yml文件中
        # if re.search('name="csrf_token" value="(.*?)"', rep.text):
        #     TokenYmlUtil().write_extract_yaml({'csrf_token': re.search('name="csrf_token" value="(.*?)"', rep.text)[1]})

        csrf_token = re.search('name="csrf_token" value="(.*?)"', rep.text)
        if csrf_token:
            TokenYmlUtil().write_extract_yaml({'csrf_token': csrf_token[1]})
            # TokenYmlUtil().write_extract_yaml(csrf_token)

    # 请求需要带请求头的接口
    @pytest.mark.parametrize("caseinfo", TokenYmlUtil().read_yaml_contents('/venv/yaml_data/login.yaml'))
    def test_login(self, caseinfo):
        # # 从extract.yml文件获取之前写入的csrf_token值
        csrf_token = TokenYmlUtil().read_extract_yaml('csrf_token')
        caseinfo['request']['data']['csrf_token'] = csrf_token
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        headers = caseinfo['request']['headers']

        # rep = RequestUtil().send_request(method, url, data=data, headers=headers)
        rep = RequestUtil().send_request(method, url, data=data, headers=headers)
        # url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        # data = {
        #     "username": "msxy",
        #     "password": "msxy",
        #     "csrf_token": csrf_token,
        #     "backurl": "http://47.107.116.139/phpwind/",
        #     "invite": ""
        # }
        # # 注意: 这步就是添加请求头, 其实就是客户端告诉服务端返回的是json格式的报文。
        # # 如果没有这部分的话,必须用print(login_rep.text),因为返回的是网页
        # # 添加下面内容后,用print(rep.json()),就能返回json格式的数据,否则print(rep.json())会报错。
        # headers = {
        #     "Accept": "application/json, text/javascript, /; q=0.01",
        #     "X-Requested-With": "XMLHttpRequest"
        # }

        # 添加完上面的请求头后,运行后发现"state"是"fail",原因是没有做cookie的鉴权
        # cookie鉴权: 网页的接口基本上都要做cookie的鉴权,
        # 所以,需要在上一步骤的test_start中先去获取到cookie值
        # 但是后面再通过get_session()方法后,就通过session,就不需要cookie了
        # rep = requests.post(url=url, data=data, headers=headers, cookies=TestSendRequest.cks)
        # rep = requests.request("post", url=url, data=data, headers=headers, cookies=TestSendRequest.cks)
        # rep = self.session.request("post", url=url, data=data, headers=headers)

        print(f"请求返回值rep.json(): {rep.json()}")

        # assert rep.json()['state'] == 'success'


if __name__ == '__main__':
    pytest.main(['-vs'])
    # pytest.main(['-vs', '--html=./report.html'])

# pytest -vs --alluredir=D:/以前の資料/workspace/pythonwork/publicdemo/venv/reports --allure-severities normal

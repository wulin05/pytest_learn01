import pytest
import requests

from publicdemo.common.common_util import CommonUtil
from publicdemo.common.requests_util import RequestUtil
from publicdemo.common.yaml_util import read_yaml


class TestApi(CommonUtil):
    session = requests.session()
    access_token = ''

    @pytest.mark.parametrize("caseinfo", read_yaml('testcases/user_manage/get_token.yaml'))
    def test_user_get_token(self, caseinfo):
        print("获取统一接口鉴权码:")
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']

        res = RequestUtil.session.request(method=method, url=url, params=data)
        print(res.json())
        TestApi.access_token = res.json()['access_token']

    @pytest.mark.parametrize("caseinfo", read_yaml('testcases/user_manage/edit_flag.yaml'))
    def test_user_edit_flag(self, caseinfo):
        print("编辑标签接口: ")
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url'] + TestApi.access_token
        data = caseinfo['request']['data']
        validate = caseinfo['validate']

        res = RequestUtil.session.request(method=method, url=url, json=data)
        print(res.json())

import requests
from publicdemo.common.common_util import CommonUtil
import pytest
from publicdemo.common.requests_util import RequestUtil
from publicdemo.common.yaml_util import read_yaml


class TestApi(CommonUtil):
    session = requests.session()

    @pytest.mark.parametrize("caseinfo", read_yaml('testcases/product_manage/get_token.yaml'))
    def test_product_get_token(self, caseinfo):
        print("获取统一接口鉴权码: ")
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']

        res = RequestUtil.session.request(method=method, url=url, params=data)
        print(res.json())

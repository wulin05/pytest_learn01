"""
本测试类是接着conftet.py之后的新一个知识点:
Pytest之parametrize()实现数据驱动
格式：
@pytest.mark.parametrize(args_name, args_value)
args_name: 参数名称,用于将参数值传递给函数
args_value: 参数值:(列表和字典列表, 元组和字典元组),有n个值,那么测试用例执行n次

发现没有,parametrize和fixture()固件中通过params参数进行传参功能是一样的,但是fixture作用倾向于前后置,而不是倾向于参数化
parametrize就是用于数据驱动。
"""

import pytest

from publicdemo.common.common_util import CommonUtil


class TestParametrize(CommonUtil):

    # @pytest.mark.parametrize('caseinfo', ['福建', '福州', '福清'])
    # def test_parametrize01(self, caseinfo):
    #     print("本节的知识点1: " + caseinfo)
    #
    # @pytest.mark.parametrize('caseinfo', ('福建', '福州', '福清'))
    # def test_parametrize02(self, caseinfo):
    #     print("本节的知识点2: " + caseinfo)
    #
    # @pytest.mark.parametrize('caseinfo', [{'name': '周杰伦'}, {'age': '18'}])
    # def test_parametrize03(self, caseinfo):
    #     print("本节的知识点3: " + str(caseinfo))  # 这边的类型要用str,所以需要对字典强转为str
    #
    # @pytest.mark.parametrize('caseinfo', [['name', '周杰伦'], ['age', '18']])
    # def test_parametrize04(self, caseinfo):
    #     print("本节的知识点4: " + str(caseinfo))  # 这边的类型同样要要用str
    #
    @pytest.mark.parametrize('arg1, arg2', [['name', '周杰伦'], ['age', '18']])
    def test_parametrize05(self, arg1, arg2):
        print("本节的知识点5: " + str(arg1) + " " + str(arg2))


if __name__ == '__main__':
    pytest.main(['-vs test_08parametrize.py'])

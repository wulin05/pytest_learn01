"""
testcases路径(包名)的product_manage(包名):这个地方注意到没有,product_manage似乎并没有符合:
pytest.ini配置文件中关于测试用例的路径(包名)规则: testpaths = ./testcases,
这是因为: 包名下可能还有包,那只要根目录(包名)testcases符合就可以,路径下的子包prodect_manage名
可以自己定义。

test_06api.py符合pytest.ini模块名: python_files = test_*.py 命名规则的需求

"""

import pytest


def read_yaml():
    return ['三年二班']
    # return ['三年二班', '晴天', '夜曲']


# 如果需要将read_yaml()函数返回值作为fixture的输入参数的话,就用下面的格式,但是后面学的一般不用这种方式来传参,
# 而是通过 @pytest.mark.parametrize(args_name, args_value) 装饰器(语法糖)方式在测试用例前使用哦!!!
# 而且由于没有传入参数了,就不能在固件中使用 request 变量了。
# @pytest.fixture(scope="function", autouse=False, name='pmp')
@pytest.fixture(scope="function", autouse=False, params=read_yaml(), ids=['S'], name='pmp')
def product_music_play(request):  # 注意传入参数request,如果没有request参数,那么在yield request.param就会报错!
    print("让音乐响起来!")
    yield request.param  # 注意返回值是使用: request.param, 而不是request.params
    print("演唱会结束!")


@pytest.fixture(scope="function", autouse=False, name='pdp')
def product_dance_play():
    print("扭动起来!")
    yield "老年迪斯科"
    print("摇累了,休息了!")

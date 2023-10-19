import pytest


def read_yaml():
    return ['chenglong', 'zengzidan', 'yangziqiong']


"""
本小节主要是说明fixture固件的params传入参数的使用
params: 实现参数化
但是,虽然fixture固件可以通过函数返回值传参,来实现参数化,但是fixture的重点在于前后置,
而,基本上是用后面章节的parametrize()装饰器(语法糖)来实现数据驱动。
"""


# 上面的方式也是ok的,但是在视频中老师是这样用法:
@pytest.fixture(scope="class", autouse=False, params=read_yaml(), ids=['c', 'z', 'y'])
# @pytest.fixture(scope="function", autouse=False, params=read_yaml(), ids=['c', 'z', 'y'], name='db')
# 如果参数使用了 name='db' 的话,那么下面class TestXiamen中的测试用例中,就不能用 exe_database_sql,要用固件别名db了。
def exe_database_sql(request):  # 注意传入参数request,如果没有request参数,那么在yield request.param就会报错!
    print("执行SQL查询")
    yield request.param  # 注意返回值是使用: request.param, 而不是request.params
    print("断开SQL链接")


class TestXiamen:

    # 如果用了name='db'的话,那么下面的exe_database_sql就要用别名db代替了!!
    def test_siming(self, exe_database_sql):
        print("测试思明区", exe_database_sql)

    def test_jimei(self, exe_database_sql):
        print("测试集美区", exe_database_sql)

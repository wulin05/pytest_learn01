"""
Pytest框架实现一些前后置（固件，夹具）的处理，常用三种:
一、setup/teardown,setup_class/teardown_class所有
二、使用@pytest.fixture()装饰器来实现部分用例的前后置: 其中用到了@pytest.mark.usefixture(固件名) 的概念
   这种主要是在@pytest.fixture()里面的参数scope="class"的时候用到,因为是固件的范围scope是class的时候,
   这种才有意义用到在测试类的前面添加 @pytest.mark.usefixture(固件名) 这种概念。
三、通过conftest.py和@pytest.fixture()结合使用实现全局的前置应用
   1.conftest.py它是专门用于存放fixtrue的配置.名称是固定的，不能变!!!
"""
import pytest

from common.common_util import CommonUtil

"""
测试使用@pytest.fixture()装饰器来实现部分用例的前后置: test_fuqing(self)
用法: @pytest.fixture(scope="",params="",autouse="",ids="",name="")
参数一、scope:作用域
    function: 在函数之前和之后执行
    class: 在类之前和之后执行
    package/session: 在整个项目会话之前和之后执行
    
参数二、autouse: 自动执行,表示:
    不需要像def test_fuqing(self, exe_database_sql)方法这样,里面写入参数exe_database_sql
    像test_fuzhou.py文件中那样,去看下就知道了。

参数三、params的作用: 具体参考test_05xiamen.py的示例
    如何把值传到Fixtrue是通过在fixtrue函数的参数里面加入request来接收参数,然后通过request.param来取值。
    (这里的param没有s): yield request.param
    
参数四、ids,不能单独使用,必须和params一起使用,作用是对参数起别名

参数五、name: 作用是给fixtrue起别名
    特别注意: 一旦使用了别名,那么fixtrue的名称就不能再用了,只能用别名
"""


@pytest.fixture(scope="function")
def exe_database_sql():
    print("\n执行SQL查询")
    yield
    print("\n关闭数据库链接")


class TestJiaoyu(CommonUtil):

    # def setup(self):   # 程序建议使用setup_method(self) 这样的写法。
    #     print("\n在每个用例之前执行一次")
    #
    # def teardown(self):
    #     print("\n在每个用例之后执行一次")
    #
    # def setup_class(self):
    #     print("\n在每个类执行前的初始化工作：比如：创建日志对象，创建数据库的连接，创建接口的请求对象。")
    #
    # def teardown_class(self):
    #     print('\n在每个类执行后的扫尾的工作：比如：销毁日志对象，销毁数据库的连接，销毁接口的请求对象。')

    def test_wulin(self):
        print("\n测试武林大佬")

    def test_minhou(self, exe_database_sql):
        print("测试闽侯")

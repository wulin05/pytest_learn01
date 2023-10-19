"""
全局conftest.py文件,针对整个项目的fixture:
1. conftest.py它是专门用于存放fixtrue的配置。conftest.py名称是固定的，不能变!!!
2. conftest.py文件代表着所有的py文件都能够直接调用conftest.py中的固件!!!
3. 项目的所有测试模块下的测试用例都能够直接调用,不需要事先在测试模块文件中导入conftest.py包,

之前在test_jiaoyu.py、test_fuzhou.py、test_04quanzhou.py、test_05xiamen.py这几个测试模块文件中,
都是在文件中直接设置了fixture固件,是为了测试 @pytest.fixture(scope, autouse, pramas, ids, name)各个参数的
含义,特别是scope范围参数: 'function'、'class'、'module'、'package/session'....
举个例子,来帮助理解:
当全局conftest.py文件中fixture固件的scope参数是 class,那么效果是: 是在测试类进行前后置处理
当全局conftest.py文件中fixture固件的scope参数是 function,那么效果是: 在每一个测试用例都有前后置处理
同理,可以理解module、package/session的范围就是在模块、包/会话级别的测试用例前后才有前后置处理

另外,@pytest.fixture()配合使用 @pytest.mark.usefixtures()的用法:
主要是因为fixture固件的参数 autouse 是False的情况,
那么通过在类、用例前面使用这个 @pytest.mark.usefixtures() 装饰器来调用fixture固件的前后置处理。
所以也就印证了一个特点: autouse不是True,那就啥都不是,看调用这个固件的测试用例的范围决定的哦。

"""
import inspect
import logging

import allure
import pytest
from _pytest.assertion.util import assertrepr_compare

from common.token_yaml_util import TokenYmlUtil


# 一般来说公共的模块conftest.py的 autouse=True,让自动运行,不在测试用例去调用,但是为了测试,这边设置为False,
# 然后在其他模块(test_06api.py、test_07user.py)中的测试用例里去调用,这样做是为了自己理解而已。
# 好好理解: function、class、module、package/session 四种作用范围!!!!!
# @pytest.fixture(scope="class", autouse=False, name='login')
# @pytest.fixture(scope="module", autouse=False, name='login')
# @pytest.fixture(scope="package", autouse=False, name='login')
# @pytest.fixture(scope="session", autouse=False, name='login')  # package 和 session是一种性质
@pytest.fixture(scope="class", autouse=False, name='login')
def login_ecshop():
    print("全局class登录前")
    yield "全局class登录中"
    print("全局class退出登录")


@pytest.fixture(scope="session", autouse=False, name='se')  # session级别的范围
def session_exe():
    print("全局session前")
    yield
    print("全局session后")


# @pytest.fixture(scope="session", autouse=True)
# def clear_yaml():
#     TokenYmlUtil().clear_extract_yaml()


# session范围应用场景: 全局测试之前要做的前置处理和全局测试结束后的后置处理
# 全局conftest.py文件的固件,只要 autouse=False,同样算个屁,也是需要在测试模块、测试类、测试用例中去手动调用
# 从这句话就可以看出,虽然你是session又怎么样,也是被局限在谁调用,就在谁的范围内!!!
# 所以,一般来说,全局conftest.py里前后置固件的autouse为True

"""
在实际的测试工作中，还会遇到一些实际问题，比如在断言时，最好【自动】添加一些日志，避免我们在测试代码中手动加入日志。
还有，最好能将断言的信息，【自动】集成到一些测试报告中，比如Allure。
这样就能避免在每一个测试脚本中手动写很多重复的代码，从而让我们将更多的时间和精力放到编写测试用例上。
有了这样的想法，接下来看看如何实现:
Pytest中提供了一个Hook函数pytest_assertrepr_compare，
这个函数会在测试脚本的assert语句执行时被调用。因此，可以实现这个函数，在函数中添加写日志和集成allure测试报告代码。

通过inspect获取调用栈信息，从中得到测试脚本中assert语句中op操作符两边的字符串名称，在日志和测试报告中会用到。
接着执行assertrepr_compare输出错误详细信息，这些信息就是在执行断言失败时的输出内容，
pytest_assertrepr_compare函数没有对其做任何修改。
接着添加了debug日志输出和allure测试报告的内容，最后再将assert的错误信息返回给调用处。
"""

# def pytest_assertrepr_compare(config, op, left, right):
#     left_name, right_name = inspect.stack()[7].code_context[0].lstrip().lstrip('assert').rstrip('\n').split(op)
#
#     pytest_output = assertrepr_compare(config, op, left, right)
#
#     logging.debug("{0} is\n {1}".format(left_name, left))
#
#     logging.debug("{0} is\n {1}".format(right_name, right))
#
#     with allure.step("校验结果"):
#         allure.attach(str(left), left_name)
#
#         allure.attach(str(right), right_name)
#
#     return pytest_output

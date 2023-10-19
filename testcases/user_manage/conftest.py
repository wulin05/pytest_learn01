import pytest


# 下面fixture固件中不需要params参数的示例,所以由于fixture没有传入参数,user_manage()括号里不需要request参数:
@pytest.fixture(scope="class", autouse=False, name='um')
def user_manage():  # 注意没有传入值,所以不需要参数request,下面的yield就没有所谓的request.param的返回值操作
    print("用户管理模块之前的准备工作")
    yield "用户管理"  # 这个地方就不是用request.param,因为没有传入参数,用不到request.param了!!!
    print("用户管理模块之后的扫尾工作")

"""
Pytest框架实现一些前后置（固件，夹具）的处理，常用三种:
一、setup/teardown,setup_class/teardown_class所有
二、使用@pytest.fixture()装饰器来实现部分用例的前后置。
三、通过conftest.py和@pytest.fixture()结合使用实现全局的前置应用
"""
import pytest


@pytest.fixture(scope="function", autouse=True)
def exe_database_sql():
    print("\n执行SQL查询")
    yield
    print("\n关闭数据库链接")


class TestFuzhou:

    def test_fuqing(self):
        print("测试福清哥")

    def test_changle(self):
        print("测试长乐鬼")

import pytest

from publicdemo.common.token_yaml_util import TokenYmlUtil


# 如果是class,代表着只在 类文件的所有用例执行之前清空extract.yml文件
# 其他module、session/package的测试用例执行前不会清空extract.yml文件
# 所以,如果想要让其他目录(例如: testcases)的测试用例也可以进行前置处理:
# 清空extract.yml文件,那么,要么写在全局的conftest.py,要么其他目录的测试用例导包后引用

# @pytest.fixture(scope="class", autouse=True)
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    TokenYmlUtil().clear_extract_yaml()



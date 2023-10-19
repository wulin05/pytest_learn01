"""
os.getcwd() 获取的是当前工作目录，不一定与脚本所在目录相同。
os.path.dirname(__file__).split('common')[0] 获取的是脚本所在的目录路径。
通常情况下，如果你希望获取脚本所在的目录，更推荐使用 os.path.dirname(__file__)，
因为它与脚本位置直接相关。但如果你需要获取当前工作目录而不考虑脚本的位置，则使用 os.getcwd() 更合适。
其实测试了，两个的效果一样的：
import os.path


def getpath():
    print(os.path.dirname(__file__))


def getpath2():
    print(os.getcwd())


getpath()
getpath2()
"""
import os
import yaml


class TokenYmlUtil:

    # 从extract.yml文件中读取存入的token
    # def read_extract_yaml(self, path, key):
    def read_extract_yaml(self, key):
        # with open(os.getcwd()+f"/{path}", mode="r", encoding="utf-8") as f:
        with open(os.getcwd() + "/extract.yml", mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 讲获取到的token值写入到extract.yaml文件
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/extract.yml", mode="a", encoding="utf-8") as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除extract.yml文件
    # 在venv目录下的conftest.py定义@pytest.fixture(score="session", autouse=True)
    # 作用是可以在本venv模块下的session级别测试用例的前置处理: 清空extract.yml的数据
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode="w", encoding="utf-8") as f:
            f.truncate()

    # 用于读取测试用例的yml文件(注意区别: read_extract_yaml()是用于读取extract.yml文件中存的token值)
    def read_yaml_contents(self, yaml_path_name):
        # with open(os.getcwd() + yaml_path_name, "r", encoding="utf-8") as f:
        # with open(os.path.dirname(__file__).split('common')[0] + yaml_path_name, "r", encoding="utf-8") as f:
        with open(os.getcwd().split('common')[0] + yaml_path_name, "r", encoding="utf-8") as f:
            yaml_data = yaml.load(stream=f, Loader=yaml.FullLoader)
            return yaml_data


if __name__ == '__main__':
    # 在当前运行下面的打印输出时,os.getcwd()获取到common的位置,所以下面的打印输出会出现文件/目录不存在的告错。
    # 在其他文件调用该方法的话，获取到其他文件运行时的文件目录: 比如test_send_request_use_yaml.py文件运行是获取
    # 到publicdemo/venv这个路径,所以对应该文件的传入参数是用/yaml_data/get_token.yaml、/yaml_data/edit_flag.yaml....没问题
    print(TokenYmlUtil().read_yaml_contents('venv/yaml_data/get_token.yaml'))
    # print(TokenYmlUtil().read_extract_yaml('access_token'))

"""
学习parametrize()之后的：YAML格式测试用例读、写、清除封装
一.yaml是一种数据格式,扩展名可以是yaml,yml,支持 # 注释,通过缩进表示层级,区分大小写。
用途:
1.用于做配置文件
2.用于编写自动化测试用例

二、yaml文件的数据组成
1.map字典对象, 使用 键: 值 表示字典
2.数组(list), 使用 '-'表示列表

三、parametrize结合yaml实现接口自动化测试


"""

import os.path

import yaml


# 获取项目的根路径path,需要导包 os.path
def get_obj_path():
    # return os.path.dirname(__file__)
    # 返回值内容是: D:\以前の資料\workspace\pythonwork\publicdemo\common
    # 再通过下面的方式就获得到了项目的根路径: D:\以前の資料\workspace\pythonwork\publicdemo\
    return os.path.dirname(__file__).split('common')[0]


# 读取yaml,需要安装pip install pyyaml库
def read_yaml(yaml_path):
    with open(get_obj_path() + yaml_path, mode='r', encoding='UTF-8') as fs:
        yaml_data = yaml.load(stream=fs, Loader=yaml.FullLoader)
        print(get_obj_path() + yaml_path)
        return yaml_data


if __name__ == '__main__':
    print(read_yaml('testcases/user_manage/get_token.yaml'))
    # read_yaml('testcases/user_manage/get_token.yaml')

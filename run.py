"""
主函数模式
(1)运行所有：pytest.main()
(2)指定模块：pytest.main(['-vs','test_login.py'])
(3)指定目录：pytest.main(['-vs','./interface_testcase'])
(4)通过nodeid指定用例运行：nodeid由模块名，分隔符，类名，方法名，函数名组
成。
pytest.main(['-vs','./interface_testcase/test_interface.py::test_04_func'])
pytest.main(['-
vs','./interface_testcase/test_interface.py::TestInterface::test_03_zhiliao'])

含义:
    使用main()方法执行测试用例,也是会调用pytest.ini的配置文件,所以pytest.ini文件的配置是核心
    命令行上可以通过一系列的参数来达到如何对测试用例进行运行:
    例如: 进入publicdemo的虚拟环境 pipenv shell 后, 执行: pytest -vs -m "smoke or product_manage or ...",效果就是
    只执行了pytest.ini 文件中的 smoke 或者 product_manage 的测试用例组

总结: 可以通过run.py文件中pytest.main()括号中的参数来进行测试, ()括号内的参数其实就是在cli命令行下: pytest .... 一样的效果
      pytest.ini配置文件是pytest测试框架的默认配置！！！

    我个人感觉： 一般就在pytest.ini文件中加 -vs 就好, 其他的我建议就用cli下加上自己想要的参数去运行
    比如: 只想运行smoke的用例： pytest -m "smoke" -n 2
"""
import os
import time

import pytest

if __name__ == '__main__':
    """
    pytest.main(['-vs']), 这里的[]内参数,就是表示可以使用命令行里的:
    -vs, -n(线程数), --reruns=num, --maxfail=num, -k(关键字:表示只有含有关键字的才被执行), --html ./path -m(冒烟用例) 
    """
    pytest.main()
    time.sleep(3)
    # os.system("allure generate ./temps -o ./reports --clean")
    # 上面的系统命令os.system是固定写法：构建allure报告,是根据当前目录的/temps里的临时文件来构建allure报告
    # 构建完成之后,通过-o 参数,输出到当前路径下的./reports目录里, --clean表示每构建一次,也要清空下./temps目录
    # 之前的临时文件,防止临时文件太多。


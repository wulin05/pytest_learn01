class TestUser:

    # um是class类,这里出现了,那从该测试用例下其他测试用例其实不会调用了,只会在测试类结束后出现后置处理。
    def test_zhangxueyou(self, um):
        print("测试张学友", "以及返回值是:" + um)

    def test_liudehua(self, um):
        print("测试刘德华", "以及返回值是:", um)

    def test_guofucheng(self, login, um):       # login是class范围,所以是从这个测试用例开始开始到本最后测试用例结束。
        print("测试郭富城", "以及返回值是:" + login, um)

    def test_liming(self, se, login):
        print("测试黎明", "以及返回值是:" + login)
        # 其实这个测试用例的login没有作用,因为是从上面的login开始。
        # 另外se是session范围,前置处理是从这个测试用例开始,
        # 后置处理是在所有测试用例完成后的最后才出现,意味着该测试用例不会出现后置处理出现哦。

    def test_final(self, se):
        print("测试test_final")
    #     # 测试发现,虽然测试用例调用了全局conftest文件的session级别的前后置处理,别名se,后置处理出现在test_empty测试用例的最后。
    #     # 因为如果是在run.py去运行的话,session是指整个项目。但是如果使用命令行运行,只对本test_07user.py模块文件运行的话
    #     # 那么就可以了,因为只执行本模块文件,这个测试过程就是一个session。
    #     # session级别的就只在全部测试用例的开头、结尾出现。

    def test_empty(self):
        print("打印空行-----------------------------------------")

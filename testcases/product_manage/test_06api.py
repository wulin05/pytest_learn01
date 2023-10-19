"""
这里补充说明下:
不知道注意到没有,不管全局conftest.py配置文件,还是各个包(product_manage、user_manage)中的conftest.py文件
的 autouse=False,
这只是我为了证明在测试类的测试用例中通过fixture固件的别名能够调用fixture固件的前后置处理。
其实,正常来说,既然都写在全局的conftest.py或各个包下的conftest.py文件了,autouse一般是设置为True,就不必这么麻烦了。
即、只要全局的conftest和包的conftest文件的autouse参数是True,所有的测试用例都不需要另外再测试用例调用别名,就可以调用
conftest固件的前后置处理了。
当然,product_manage包下的测试类的测试用例是不会跨包执行user_manage包下的conftest文件的fixture固件的前后置处理,
除非,导入user_manage包下的conftest,那么product_manage包下的测试类的测试用例就能够调用了!
这段话,可以参考最下面的 def test_05_other_conftest(self, um) 这个测试用例。
"""

from publicdemo.testcases.user_manage.conftest import *


# @pytest.mark.usefixtures("um")
class TestApi:

    def test_01_listen_music(self, pmp):
        # print("通过conftest.py里的fixture固件pmp:来听我的演唱会" + pmp)
        print("通过conftest.py里的固件fixture固件pmp: 来听我的演唱会", pmp)

    def test_02_listen_music(self):
        # 这个测试用例参数中没有conftest.py中的任何fixture固件
        # 所以该测试用例没有前后置处理,只是简单地输出: 来听我的演唱会 PASSED 就结束了。
        print("没有使用fixture的固件前后置处理: 来听我的演唱会")

    def test_03_play_dance(self, pdp):
        # 这个测试是为了调用conftest.py文件中fixture固件pdp: 一起摇摆!
        # print("调用conftest.py里的fixture固件pdp:一起摇摆!")
        print("调用conftest.py文件中的fixture固件pdp: 一起摇摆!", pdp)

    def test_04_full_test(self, login, pmp, pdp):
        print("测试用例调用了全局的conftest.py的'login'固件以及当前目录下的conftest.py的两个固件:"
              "pmp、pdp: 先'登录前',然后'让音乐响起来',再'扭动起来!',再输出上面的print语句,"
              "然后'摇累了,休息了!','演唱会结束'", login, pmp, pdp)
        # 注意,由于后面我将全局conftest.py模块文件中的fixture中login固件的scope值设置为class,
        # 所以,"全局class退出登录"这个后置处理输出是在这个类都完成后,才会输出,即、
        # 在本例中是在 test_05_other_conftest这个测试用例的最后能够找"全局class退出登录"

    # @pytest.mark.usefixtures("um")
    # def test_05_other_conftest(self):
    def test_05_other_conftest(self, um):
        # def test_05_other_conftest(self, um)这个方式,不需要from testcases.user_manage.conftest import *
        # 并且,不需要@pytest.mark.usefixtures("um")装饰器,同样能够调用到"um"的固件,虽然不在一个本包目录下
        print("该测试用例在没有导入user_manage包路径下的conftest模块的情况下,这里是否能够直接调用别名为'um'的固件?")
        # 结果显示error,说明在没有导包的情况,无法调用user_manage路径下的conftest.py模块下的fixture固件的前后置处理
        # 也就是必须 from testcases.user_manage.conftest import *
        # 才可以在类的开头使用装饰器(语法糖),但是如果是在类的开头使用装饰器,那么该类下的所有用例都会执行。
        # 所以,也可以就只在本测试用例中使用装饰器(语法糖)来调用,更精准地应用。

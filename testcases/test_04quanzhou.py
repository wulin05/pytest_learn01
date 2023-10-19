import pytest

"""
这里主要说明@pytest.fixture(scope="class", autouse=False)中scope="class"和"function"的区别：
1.如果使用function就没得说的,而且autouse=True的话,下面所有的测试类都不需要def test_fengze(self, exe_web_auth)
直接def test_fengze(self),所有的测试用例就都有前后置处理了。
2.如果使用function,而且autouse=False的话,那么就要在想要有前后置处理的测试用例中添加exe_web_auth参数
例如: def test_fengze(self, exe_web_auth)
3.如果使用class,那么当然你也可以在每个测试用例去def test_fengze(self, exe_web_auth)添加exe_web_auth参数,
但是既然是用class类了,那么就用类的思维去设定:
既然是pytest.fixture的scope参数是class,那么就在测试类的前面使用装饰器(语法糖)就好了,这样该装饰器(语法糖)下的类,
就都有前后置处理了。
如下:
@pytest.mark.usefixtures(exe_web_auth)

但是这里我需要补充下: 
def exe_web_auth()这个前后置处理类里面有yield "very good"这个代码,表示该类有返回值"very good",
虽然class Test04Zhangzhou这个类使用了@pytest.mark.usefixtures("exe_web_auth")这个装饰器(语法糖),
但是如果class Test04Zhangzhou这个类的两个测试方法test_xiangcheng(self)、test_longwen(self),想要调用
到这个返回值,那么还得像class Test04Quanzhou类那样,在def test_fengze(self, exe_web_auth)测试用例中传入
参数exe_web_auth才能使用到返回值: print(exe_web_auth)

"""


@pytest.fixture(scope="class", autouse=False)
def exe_web_auth():
    print("登录web认证界面")  # 这个是前置处理
    # return "success"   # return后面的内容是没有效果的,所以可以用yield,yield后面还可以有其他内容
    yield "very good"  # 这个相当于有返回值,并且还能继续使用下面的print("关闭web链接")语句
    """而且如果想要使用到这个very good返回值,def test_longwen(self)里面必须添加exe_web_auth参数"""
    print("关闭web链接")  # 这个是后置处理


# def read_yaml():
#     return ['chenglong', 'zengzidan', 'yangziqiong']
#
#
# @pytest.fixture(scope="class", autouse=False, params=read_yaml(), ids=['c', 'z', 'y'])
# def exe_web_auth_02(request):
#     print("登录web认证界面")
#     yield request.param
#     print("关闭web链接")


# 注意这个输出的结果,由于fixture的scope参数值是:class,尽管autouse=False,但是在Test04Quanzhou这个测试类里
# 的两个测试用例 test_fengze()、test_liceng()的开头和结尾：
# 有"登录web认证界面"和结尾的"关闭web链接"两个前后置处理,
# 而不是每一个测试用例的开头和结尾哦!!!!! 注意理解哦!!!!!不理解的话,运行run.py,再观察下哦!!!!!
# 测试用例中如果有 exe_web_auth 参数,那么测试用例就会有"登录web认证界面"和结尾的"关闭web链接"两个前后置处理
# 并且可以通过 exe_web_auth 参数来获取fixture固件的返回值: yield "very good" 和 yield request.param
# fixture固件返回值的两种情况:
# 1.有传入参数: yield request.param  参考上面的 def exe_web_auth_02()这个固件,其实后续章节就有说明了,我这边又多费一次口舌,加深记忆
# 2.无传入参数: yield "返回值"
class Test04Quanzhou:

    def test_fengze(self, exe_web_auth):
        print("测试丰泽区")
        print(exe_web_auth)

    def test_liceng(self, exe_web_auth):
        print("测试鲤城区")
        print(exe_web_auth)


""" 
本节的核心是要说明的内容: @pytest.mark.usefixtures("exe_web_auth"):  
其实本节的 @pytest.mark.usefixtures("exe_web_auth")没有什么太大意义,因为fixture固件是定义在本文件中,
不用这个 @pytest.mark.usefixtures("exe_web_auth") ,只要fixture的autouse=True的话,
默认 该文件下的所有类 都会自动运行 fixture固件的前后置处理, 但是这里用了 autouse=False,所以,才有必要
在类的前面使用 @pytest.mark.usefixtures("exe_web_auth"),来让有这个装饰器的类自动使用这个fixture固件进行前后置处理。
"""


# 下面的@pytest.mark.usefixtures("exe_web_auth")没有注释掉的情况下:
# 会在整个Test04Zhangzhou的类的开头有"登录web认证界面"前置处理和结尾有"关闭web链接"后置处理。
# 但是,如果把下面的装饰器注释掉了,那么注意看输出结果: test_xiangcheng(self)这个测试用例,没有fixture固件的前后置处理
# 即、没有"登录web认证界面"和结尾的"关闭web链接"两个前后置处理
# test_longwen(self, exe_web_auth)因为有 exe_web_auth 参数,所以,该测试用例
# 在开头有"登录web认证界面"和结尾的"关闭web链接"两个前后置处理,并且print(exe_web_auth)可以获取到传入参数: very good
@pytest.mark.usefixtures("exe_web_auth")
class Test04Zhangzhou:

    def test_xiangcheng(self):  # 如果没有exe_web_auth参数,就不会调用到fixture固件的前后置处理了,虽然它的scope="class"
        print("漳州芗城区")
        print(exe_web_auth)  # <function exe_web_auth at 0x00000272EA7B2020>

    def test_longwen(self, exe_web_auth):
        print("漳州龙文区")
        print(exe_web_auth)  # very good

class CommonUtil:
    pass
    """
    下面的被注释掉的是:
    Pytest框架实现一些前后置（固件，夹具）的处理，常用三种的第一种
    一、setup_method/teardown_method,setup_class/teardown_class所有
    其核心思想就是创建common包的common_util模块的CommonUtil类,给testcases包下的
    test_jiaoyu.py 和 test_mashang.py 下的所有测试用例都要使用的话,这样的导入的方式
    可以减轻工作量: 比如不仅仅 test_jiaoyu.py 和 test_mashang.py,还有几十、几百个文件也需要,
    那就不能像 test_jiaoyu.py 和 test_mashang.py文件中,每一个文件中去写入,那得累死,
    所以使用导包的方式!!!
    
    但是,由于可能实际中只有部分的测试用例需要用到这种前后置的处理,比如(我只是举例子):
    在test_jiaoyu.py中需要对class TestJiaoyu(CommonUtil)类才需要这种前后置处理,那我就把这边注释了,免得
    测试的时候test_mashang.py也会输出一大堆内容,不好观察test_jiaoyu.py的输出内容。
    所以,CommonUtil这个类被我用pass关键字了,这样虽然test_jiaoyu.py和test_mashang.py
    虽然都导入了父类: CommonUtil,但是
    由于这边被使用了pass,所以就不会有下面的前后置内容输出,便于观察。
    
    如果为了测试前后置处理的第一种,就把下面的注释去掉,不用再去test_jiaoyu.py和test_mashang.py里进行导包,
    继承父类的操作,直接进行测试就行!
    """
    def setup_method(self):
        print("\n在每个用例之前执行一次")

    def teardown_method(self):
        print("\n在每个用例之后执行一次")

    def setup_class(self):
        print("\n在每个类执行前的初始化工作：比如：创建日志对象，创建数据库的连接，创建接口的请求对象。")

    def teardown_class(self):
        print('\n在每个类执行后的扫尾的工作：比如：销毁日志对象，销毁数据库的连接，销毁接口的请求对象。')

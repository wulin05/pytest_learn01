import pytest

from common.common_util import CommonUtil


class TestMashang(CommonUtil):
    # def setup(self):
    #     print("\n在每个用例之前执行一次")
    #
    # def teardown(self):
    #     print("\n在每个用例之后执行一次")
    #
    # def setup_class(self):
    #     print("\n在每个类执行前的初始化工作：比如：创建日志对象，创建数据库的连接，创建接口的请求对象。")
    #
    # def teardown_class(self):
    #     print('\n在每个类执行后的扫尾的工作：比如：销毁日志对象，销毁数据库的连接，销毁接口的请求对象。')

    """@pytest.mark.smoke表示pytest.ini配置文件中有smoke测试用例组,
    在哪个方法上面有这个装饰器,就代表这个方法属于这个测试用例组
    """

    @pytest.mark.smoke
    def test_baili(self):
        # time.sleep(3)
        print("测试百里老师")
        # raise Exception("百里老师又开车了?")
        assert 1 == 1

    @pytest.mark.product_manage
    def test_yiran(self):
        # time.sleep(3)
        print("测试依然老师")
        # raise Exception("依然老师又开车了?")
        assert 'a' in 'abc'

    @pytest.mark.user_manage
    def test_xingyao(self):
        print("测试星瑶老师")
        flag = True
        assert flag is True

    # 这个skip是系统提供的,不是人为在pytest.ini配置文件中定义的
    # 演示无理由跳过
    @pytest.mark.skip(reason="无理由跳过")
    def test_linwu(self):
        print("测试无理由跳过skip")

    # 演示有理由跳过
    workable = 8

    @pytest.mark.run(order=1)
    @pytest.mark.skipif(workable < 10, reason="工作年限小于10年,跳过")
    def test_workable(self):
        print("测试有理由跳过: 工作年限小于10年")

# 一般不会在测试用例里写下面的main(),一般是在项目的路径下创建run.py文件中,去写main()的测试用例
# if __name__ == '__main__':
#     pytest.main(['-vs'])

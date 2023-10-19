

### 一、关于setup、teardown、setup_class、teardown_class、fixture、conftest优先级
#### 1.
####  前提在fixture、conftest的配置中autouse为True的情况：

##### 会话： fixture的session级别的优先级最高

##### 类： fixture的class级别的优先级高于setup_class
##### 类： setup_class

##### 函数： fixture的function级别的优先级高于setup
##### 函数： setup

#### 以上是老师课程的总结

##### 2. 注意注意,以下结论是基于 conftest.py和conftest.py中的fixture固件的autouse=True的情况下
#####    (如果fixture的autouse=False,主要是看在哪里被调用，当然也看score="functiong/class/module/session"的范围喽
#####    关于这个,可以具体参考test_07user.py模块的示例,可能更容易明白)
##### 我的理解是：
在全局conftest和局部的conftest的固件的scope值相同的情况下:

①、全局conftest比局部的conftest的优先级高

②、如果全局conftest模块某个固件的scope范围是function,那肯定不会比局部
   conftest模块中的固件scope范围是class的高,也比setup_class/teardown_class低!!!!

③、同样setup_class/teardown_class优先级要比 全局conftest/局部conftest的scope=function
   的优先级要高,在全局conftest和局部conftest的scope=class的时候,才是
   全局conftest > 局部conftest > setup_class/teardown_class

### 总结来说：
setup、teardown、setup_class、teardown_class、fixture、conftest优先级的比较如下:

全局conftest.py文件fixture的scope=package/session > 
局部conftest.py文件fixture的scope=package/session >
本文件中fixture的scope=package/session >

全局conftest.py文件fixture的class >
局部conftest.py文件fixture的class > 
本文件中fixture的class >
setup_class/teardown_class >

全局conftest.py文件fixture的function >
局部conftest.py文件fixture的function > 
本文件中fixture的function>
setup/teardown

其实还有一个层级：比如在testcases模块下创建一个conftest.py文件,那就介于全局conftest
和 product_manage/user_manage这两个局部conftest.py的优先级之间了。

------------------------------------------------------------------------------
#####################################

### 二、关于pytest的执行过程：

1.查询publicdemo项目testcases目录下的全局conftest.py文件
2.查询publicdemo项目testcases目录下的pytest.ini文件,找到测试用例的位置
3.查询用例目录(product_manage/user_manage)下的局部conftest.py文件
4.查询测试用例文件是否有setup,teardown,setup_class,teardown_class：比如common包下的common_util.py文件中包含了这些前后置处理
5.最后根据pytest.ini文件的测试用例的规则去查找用例并执行



【Python】Playwright - 自动化Web测试框架,来自微软公司的无头浏览器
============================================================

## 知识点

* 网页自动化测试框架 - Playwright for python 3
* 可以继续去自动抢票了

## 官网
https://playwright.dev/

# 实战演习

``` 
# 初始化Python3虚拟环境
$ python3 -m venv myapp
python3 -m venv myapp:
这是用于创建 Python 虚拟环境的命令。
python3 表示使用 Python 3 的版本来创建虚拟环境。
-m venv 表示使用 Python 的 venv 模块来创建虚拟环境。
myapp 是虚拟环境的名称，你可以根据自己的项目需求来命名。
该命令创建了一个独立的 Python 环境，可以在其中安装项目所需的包，以确保包的版本不会与全局 Python 环境中的包发生冲突。

pipenv --python 3.11.4:
这是 Pipenv 工具的命令，用于创建项目的虚拟环境，并指定要使用的 Python 版本。
--python 3.11.4 表示创建虚拟环境时要使用 Python 3.11.4 版本。
Pipenv 是一个 Python 项目管理工具，它结合了依赖管理（使用 Pipfile 和 Pipfile.lock）和虚拟环境管理（使用 virtualenv）的功能。
它的目标是简化 Python 项目的依赖管理和环境配置。

总之，两者的主要区别在于使用的工具和目的。python3 -m venv 是 Python 自带的创建虚拟环境的命令，
而 pipenv 是一个独立的项目管理工具，它可以创建虚拟环境并管理项目依赖。选择哪个命令取决于你的项目需求和偏好。
如果你只需要创建虚拟环境，那么第一个命令足够；如果你需要更全面的项目管理功能，可以考虑使用 Pipenv。

$ ./myapp/Scripts/activate  (cmd)
$ ./myapp/Scripts/Activate.sp1  (powershell)
## 这是激活虚拟环境的命令。一旦激活，你将进入虚拟环境的环境中，你的命令行提示符可能会更改以显示你当前处于哪个虚拟环境。
## 在激活的虚拟环境中，你可以安装和运行 Python 包，这些包将与虚拟环境关联，而不会影响全局 Python 环境。

$ pip list
接下来如果需要,去更新环境包
$ python -m pip install --upgrade pip
$ python -m pip install --upgrade setuptools

# 安装Playwright
$ pip install playwright==1.


# 团队共享
requirement.txt生成方法
pip freeze > requirements.txt
安装requirement.txt内依赖
pip install -r requirement.txt

```
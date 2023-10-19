### 链接
https://www.youtube.com/watch?v=Ib1vO2Tbogo

### publicdemo目录是使用pipenv方式创建的虚拟环境,所以进入虚拟环境的命令是：
* pipenv shell  (注意要到当前publicdemo目录去运行该命令)



```bash
$ mkdir myweb

$ cd myweb
```

## 项目初始化：

* pipenv以是基于项目的,使用cd/d命令进入到项目路径中,然后使用pipenv --python 版本号  命令创建基于Python3的虚拟环境。
  创建虚拟环境后，在项目文件夹下会自动生成Pipfile文件。

```bash
$ pipenv --python 3.11.4   项目初始化：
$ pipenv install flask     安装flask库
$ cat Pipfile				
$ pip list
$ pipenv shell          激活虚拟环境(也叫进入虚拟环境)
$ pip list
$ pipenv --venv         查看当前虚拟环境名
$ pipenv graph			查看安装的依赖、库
$ exit

```

## 安装开发专用包
* 不要使用pip安装库，而要使用pipenv install命令
```bash
$ pipenv install --dev requests

$ cat Pipfile
```

## 延伸
```bash
$ pipenv run pip list
```

## 团队内项目共享
将建立好的Pipfile文件直接拷贝给项目组的其他成员,可迅速完成开发环境的搭建
```bash
$ mkdir myweb1
$ cd myweb1
```

# 安装依赖库,包括开发用依赖库
## 将Pipfile直接拷贝到myweb1目录下
```bash
$ pipenv install --dev
$ pipenv shell
$ pip list
$ exit
```

## 删除虚拟环境
```bash
$ pipenv --rm

$ pipenv --venv
```

## 代码运行

### main.py
```bash
$ pipenv run python main.py
```

## 定义执行脚本

### Pipfile

```
[scripts]
start = "python main.py"
test = "pytest"
list = "pip list"
```

### 在Pipfile脚本中添加了上面的内容后,就可以直接在本地的项目目录执行
```
$ pipenv run start
$ pipenv run pytest
$ pipenv run list
```



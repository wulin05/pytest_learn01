# 一、URL
1.URL： 是互联网上标准资源的地址,一般称为统一资源定位符
2.组成： 协议：//hostname[:port]/path/[?查询参数1 & 查询参数2]
3.示例： http://kdtx-test.itheima.net:8080/contract/details?id=449280106&pageType=info
https://kdtx-test.itheima.net/#/login 普达天下

# 二、HTTP协议
1. HTTP：超文本传输协议，基于请求与响应的应用层协议
2. 作用：规定了客户端和服务器之间信息传递规范，是而在共同遵守的协议
3. 组成：
       1.HTTP请求：定义请求数据格式
         请求行、请求头、请求体
       2.HTTP相应：定义相应数据格式
         状态行、相应头、相应体
-------------------------------------------
1.HTTP请求-请求行：
位置： 请求数据第一行
作用： 说明请求方法、访问的资源、协议版本

      POST http://kdtx-text.itheima.net/api/login HTTP/1.1     -----> 第一行是 请求行，但是HTTP/1.1是状态行
      HOST: KDTX-test.itheima.net
      User-Agent: Mozilla/5.0(windows NT10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Geck)
      Chrome/108.0.0.0 Safari/537.36
      Content-Type: application/json;charset=UTF-8              -----> 第二行到这一行就是 请求头

      {"username":"namager","password":"123456","code":"2","uuid":"ea3.。。。。bfdc"}
                                                               -----> 上面一行是 请求体
常用请求方法：
      GET: 从服务器获取资源
      POST: 在服务器新建一个资源
      PUT: 在服务器更新资源
      DELETE: 从服务器删除资源

2.HTTP请求-请求头
位置： 请求数据第二行到空白行之间
作用： 通知服务器客户端请求信息
特点： 请求头部由 键值对 组成，每行一对
Content-Type: 请求体数据类型
   ① test/html： HTML格式
   ② image/jpeg： jpg图片格式
   ③ application/json： JSON数据格式
   ④ application/x-www-form-urlenconded： 表单默认的提交数据格式
   ⑤ multipart/form-data： 在表单中进行文件上传时使用

3.HTTP请求-请求体
位置： 空白行之后的内容
作用： 传输数据实体
注意： 请求体常在POST、PUT方法中使用
常配合的请求头： Content-Type 和Content-Length
* 另外，请求报文中可以没有请求体数据。即、不是所有的请求方法都有请求体, 比如GET/DELETE方法就没有请求体数据

4.HTTP响应-状态行
位置： 响应数据第一行 
作用： 描述服务器处理结果
内容： 状态行由协议版本号、状态码、状态消息组成

例如：
    HTTP/1.1 200 OK    -----> HTTP/1.1：协议版本号、200：状态码、ok：状态信息
    Server: nginx
    Date: Fri,23 Dec 2022 07:50:55 GMT
    Content-Type: application/json
    Content-Length: 228

    {"msg":"操作成功","code":200,"token":"eyjhbGciwuVop9EBH_aM9BvBld4blHzDvljLNoCwtng"}

状态码： 三位数字组成、第一个数字定义响应类别
    1xx: 指示信息
    2xx: 成功
    3xx: 重定向
    4xx: 客户端错误
    5xx: 服务端错误

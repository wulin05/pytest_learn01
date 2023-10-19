import json

import requests


class RequestUtil:
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        if method == "get":
            print("---------接口测试开始----------")
            print(f"请求方式: {method}")
            print("请求地址: %s" % url)
            print("请求参数: %s" % data)

            # res = requests.session().request(method, url, params=data, **kwargs)
            # 上面的含义是:创建一个Session对象request.session(),使用该对象的request()方法发出一个HTTP请求
            res = self.session.request(method, url, params=data, **kwargs)
            print(f"请求返回值res.text: {res.text}")
            print("请求结束")
            print("\n")
        else:
            print("---------接口测试开始----------")
            print(f"请求方式: {method}")
            print("请求地址: %s" % url)
            print("请求参数: %s" % data)

            # 如果是"post"请求,有两种传参方式: data 和 json,所以为了避免不同的参数格式,所以就统一转换成str,通过data方式传参
            # data支持str和简单dict、json就只能支持键值对的str。
            # data = json.dumps(data)
            # 这里注释掉,是因为在上传文件的用例,是files参数,所以调用此send_request方法会出错,其实注释掉的话,就没有if...else的必要了
            res = self.session.request(method, url, data=data, **kwargs)
            print(f"请求返回值res.text: {res.text}")
            print("请求结束")
            print("\n")

        return res
        # return res.text

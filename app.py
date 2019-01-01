from wsgiref.simple_server import make_server
from webob import Response, Request
from webob.dec import wsgify
from webob.exc import HTTPNotFound


# application函数不用了, 用来和app函数对比
# def application(environ: dict, start_response):
#     # 请求处理
#     request = Request(environ)
#     print(request.method)
#     print(request.path)
#     print(request.query_string)
#     print(request.GET)
#     print(request.POST)
#     print("params = {}".format(request.params))
#
#     # 响应处理
#     res = Response()  # [("Content-Tyep", "text/html; charset=UTF-8"), ("Content-Length", "0")]
#     res.status_code = 200
#     print(res.content_type)
#     res.body = "<h1>this is my web root!</h1>".encode("utf-8")
#     return res(environ, start_response)


class Application:
    ROUTETABLE = {}

    @classmethod  # 注册， 装饰器
    def register(cls, path):
        def wrapper(handler):
            cls.ROUTETABLE[path] = handler
            return handler
        return wrapper

    @wsgify
    def __call__(self, request: Request) -> Response:
        try:
            return self.ROUTETABLE.get(request.path)(request)
        except:
            raise HTTPNotFound('<h1>你访问的页面被外星人劫持了</h1>')


@Application.register('/')
def index(request: Request):
    res = Response()
    res.status_code = 200
    res.content_type = "text/html"
    res.charset = "utf-8"
    res.body = "<h1>root!</h1>".encode()
    return res


@Application.register('/python')
def index(request: Request):
    res = Response()
    res.status_code = 200
    res.content_type = "text/plain"
    res.charset = "gb2312"
    res.body = "<h1>python</h1>".encode()
    return res


if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 8000
    server = make_server(ip, port, Application())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()

from wsgiref.simple_server import make_server
from webob import Response, Request
from webob.dec import wsgify


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


@wsgify
def app(request: Request) -> Response:
    print(request.method)
    print(request.path)
    print(request.query_string)
    print(request.GET)
    print(request.POST)
    print("params = {}".format(request.params))

    res = Response()
    res.body = "<h1>this is my web root!</h1>".encode("utf-8")
    return res


if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 8000
    server = make_server(ip, port, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()

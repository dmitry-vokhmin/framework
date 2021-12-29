from quopri import decodestring
from .requests import GetRequest, PostRequest


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 Page Not Found'


class Framework:

    def __init__(self, routes, middlewares):
        self.routes = routes
        self.middlewares = middlewares

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        request = {}

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = self.decode_value(data)
            print(f'Нам пришёл post-запрос: {Framework.decode_value(data)}')
        elif method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = self.decode_value(request_params)
            print(f'Нам пришли GET-параметры:'
                  f' {Framework.decode_value(request_params)}')

        for middleware in self.middlewares:
            middleware(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data

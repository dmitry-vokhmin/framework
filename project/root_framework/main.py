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
        for middleware in self.middlewares:
            middleware(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

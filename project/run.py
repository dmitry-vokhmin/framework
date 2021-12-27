from wsgiref.simple_server import make_server
from project.root_framework import Framework
from project.urls import routes, middlewares


application = Framework(routes, middlewares)


with make_server('', 8080, application) as httpd:
    print('Сервер запустился')
    httpd.serve_forever()

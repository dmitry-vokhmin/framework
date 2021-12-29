from wsgiref.simple_server import make_server


def parse_input_data(data):
    result = {}
    if data:

        params = data.split('&')
        for item in params:

            k, v = item.split('=')
            result[k] = v
    return result


def application(environ, start_response):
    query_string = environ['QUERY_STRING']
    print(query_string)  # -> 'id=1&category=10'
    request_params = parse_input_data(query_string)
    print(request_params)  # -> {'id': '1', 'category': '10'}
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'Hello world from a simple WSGI application!']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

from wsgiref.simple_server import make_server


def parse_input_data(data: str):
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env) -> bytes:
    # получаем длину тела, они приходит в строковом формате
    content_length_data = env.get('CONTENT_LENGTH')
    # приводим к int, если тело есть, иначе возвращаем 0
    content_length = int(content_length_data) if content_length_data else 0
    # считываем данные если они есть
    data = env['wsgi.input'].read(content_length) \
        if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        # декодируем данные
        data_str = data.decode(encoding='utf-8')
        print(data_str)  # 'id=1&category=10'
        # собираем их в словарь
        result = parse_input_data(data_str)
    return result


def application(environ, start_response):
    # получаем данные
    data = get_wsgi_input_data(environ)
    # превращаем данные в словарь
    data = parse_wsgi_input_data(data)
    print(data)  # -> {id: 1, category: 10}
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'Hello world from a simple WSGI application!']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

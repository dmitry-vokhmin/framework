from abc import ABC, abstractmethod


class RequestFactory(ABC):
    @staticmethod
    def _parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @abstractmethod
    def get_request_params(self, environ):
        pass


class GetRequest(RequestFactory):
    def get_request_params(self, environ):
        query_string = environ['QUERY_STRING']

        return self._parse_input_data(query_string)


class PostRequest(RequestFactory):
    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        data = b''
        if content_length_data:
            data = env['wsgi.input'].read(int(content_length_data))
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self._parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)

        return self.parse_wsgi_input_data(data)
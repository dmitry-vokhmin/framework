from time import time


class AppRoute:
    def __init__(self, routes, url):
        self.url = url
        self.routes = routes

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debug:
    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def timeit(method):
            def timed(*args, **kwargs):
                ts = time()
                result = method(*args, **kwargs)
                te = time()
                delta = te - ts
                print(f"Time: {delta}")
                return result
            return timed
        return timeit(cls)

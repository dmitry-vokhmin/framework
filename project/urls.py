from datetime import datetime


def add_datetime(request):
    request['datetime'] = datetime.now()


middlewares = [add_datetime]

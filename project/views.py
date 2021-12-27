from project.root_framework import render


class Index:
    def __call__(self, request: dict):
        return '200 OK', render('index.html', **request)


class Contacts:
    def __call__(self, request):
        return '200 OK', render('contact.html', **request)


class Examples:
    def __call__(self, request):
        return '200 OK', render('examples.html', **request)


class AnotherPage:
    def __call__(self, request):
        return '200 OK', render('another_page.html', **request)


class Page:
    def __call__(self, request):
        return '200 OK', render('page.html', **request)

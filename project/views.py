from project.root_framework import render
from project.patterns.creational_patterns import Engine, Logger
from project.patterns.structural_patterns import AppRoute, Debug
from project.patterns.behavioral_patterns import (
    TemplateView,
    CreateView,
    ListView,
    EmailNotifier,
    SmsNotifier,
    BaseSerializer
)

site = Engine()
logger = Logger('main')
email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()

routes = {}


@AppRoute(routes, '/')
class Index:
    @Debug('index')
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.shops)


@AppRoute(routes, '/contacts/')
class Contacts:
    @Debug('contacts')
    def __call__(self, request):
        return '200 OK', render('contact.html', **request)


@AppRoute(routes, '/examples/')
class Examples:
    @Debug('examples')
    def __call__(self, request):
        return '200 OK', render('examples.html', **request)


@AppRoute(routes, '/another_page/')
class AnotherPage:
    @Debug('another_page')
    def __call__(self, request):
        return '200 OK', render('another_page.html', **request)


@AppRoute(routes, '/page/')
class Page:
    @Debug('page')
    def __call__(self, request):
        return '200 OK', render('page.html', **request)


@AppRoute(routes, '/product-list/')
class ProductList:
    @Debug('product-list')
    def __call__(self, request):
        logger.log('Список продуктов')
        try:
            id_ = int(request['request_params']['id'])
            shop = site.find_shop_by_id(id_)
            return '200 OK', render('product_list.html', objects_list=shop.products, name=shop.name, id=shop.id)
        except KeyError:
            return '200 OK', 'No products have been added yet'


@AppRoute(routes, '/create-product/')
class CreateProduct:
    shop_id = -1

    @Debug('create-product')
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            if self.shop_id != -1:
                shop = site.find_shop_by_id(self.shop_id)
                product = site.create_product('laptop', name, shop)
                site.products.append(product)

                product.observers.append(email_notifier)
                product.observers.append(sms_notifier)

                return '200 OK', render('product_list.html',
                                        objects_list=shop.products,
                                        name=shop.name,
                                        id=shop.id)
        else:
            try:
                self.shop_id = int(request['request_params']['id'])
                shop = site.find_shop_by_id(self.shop_id)

                return '200 OK', render('create_product.html',
                                        name=shop.name,
                                        id=shop.id)
            except KeyError:
                return '200 OK', 'No shops have been added yet'


@AppRoute(routes, '/create-shop/')
class CreateShop:
    @Debug('create-shop')
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            new_shop = site.create_shop(name)
            site.shops.append(new_shop)

            return '200 OK', render('index.html', objects_list=site.shops)
        else:
            shops = site.shops

            return '200 OK', render('create_shop.html',
                                    shops=shops)


@AppRoute(routes, '/shop-list/')
class ShopList:
    @Debug('shop-list')
    def __call__(self, request):
        logger.log('Список магазинов')
        return '200 OK', render('shops_list.html',
                                objects_list=site.shops)


@AppRoute(routes, '/copy-product/')
class CopyProduct:
    @Debug('copy-product')
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']

            old_product = site.get_product(name)
            if old_product:
                shop = old_product.shop
                new_name = f'copy_{name}'
                new_product = old_product.clone()
                new_product.name = new_name
                new_product.shop = shop
                shop.products.append(new_product)

                site.products.append(new_product)

                return '200 OK', render('product_list.html',
                                        objects_list=site.products,
                                        name=new_product.shop.name,
                                        id=new_product.shop.id)
        except KeyError:
            return '200 OK', 'No product have been added yet'


@AppRoute(routes=routes, url='/buyer-list/')
class BuyersListView(ListView):
    queryset = site.buyers
    template_name = 'buyer_list.html'


@AppRoute(routes=routes, url='/create-buyer/')
class BuyerCreateView(CreateView):
    template_name = 'create_buyer.html'

    def create_obj(self, data: dict):
        name = data['name']
        name = site.decode_value(name)
        new_obj = site.create_user('buyer', name)
        site.buyers.append(new_obj)


@AppRoute(routes=routes, url='/add-buyer/')
class AddProductToBuyerCreateView(CreateView):
    template_name = 'add_buyer.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['products'] = site.products
        context['buyers'] = site.buyers
        return context

    def create_obj(self, data: dict):
        product_name = data['product_name']
        product_name = site.decode_value(product_name)
        product = site.get_product(product_name)
        buyer_name = data['buyer_name']
        buyer_name = site.decode_value(buyer_name)
        buyer = site.get_buyer(buyer_name)
        product.add_buyer(buyer)


@AppRoute(routes=routes, url='/api/')
class ProductApi:
    @Debug(name='ProductApi')
    def __call__(self, request):
        return '200 OK', BaseSerializer(site.products).save()

from project.root_framework import render
from project.patterns.creational_patterns import Engine, Logger


site = Engine()
logger = Logger('main')


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=site.shops)


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


class ProductList:
    def __call__(self, request):
        logger.log('Список продуктов')
        try:
            id_ = int(request['request_params']['id'])
            shop = site.find_shop_by_id(id_)
            return '200 OK', render('product_list.html', objects_list=shop.products, name=shop.name, id=shop.id)
        except KeyError:
            return '200 OK', 'No products have been added yet'


class CreateProduct:
    shop_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            if self.shop_id != -1:
                shop = site.find_shop_by_id(self.shop_id)
                product = site.create_product('laptop', name, shop)
                site.products.append(product)
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


class CreateShop:
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


class ShopList:
    def __call__(self, request):
        logger.log('Список магазинов')
        return '200 OK', render('shops_list.html',
                                objects_list=site.shops)


class CopyProduct:
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


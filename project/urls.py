from datetime import datetime
from project.views import (
    Index,
    Contacts,
    Examples,
    AnotherPage,
    Page,
    CreateShop,
    CreateProduct,
    ShopList,
    ProductList,
    CopyProduct
)


def add_datetime(request):
    request['datetime'] = datetime.now()


middlewares = [add_datetime]

routes = {
    '/': Index(),
    '/contacts/': Contacts(),
    '/examples/': Examples(),
    '/another_page/': AnotherPage(),
    '/page/': Page(),
    '/product-list/': ProductList(),
    '/create-product/': CreateProduct(),
    '/create-shop/': CreateShop(),
    '/shop-list/': ShopList(),
    '/copy-product/': CopyProduct()
}

from copy import deepcopy
from quopri import decodestring


class User:
    pass


class Seller(User):
    pass


class Buyer(User):
    pass


class UserFactory:
    types = {
        'seller': Seller,
        'buyer': Buyer
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class ProductPrototype:

    def clone(self):
        return deepcopy(self)


class Product(ProductPrototype):

    def __init__(self, name, shop):
        self.shop = shop
        self.name = name
        self.shop.products.append(self)


class Laptop(Product):
    pass


class Phone(Product):
    pass


class ProductFactory:
    type = {
        'laptop': Laptop,
        'phone': Phone
    }

    @classmethod
    def create(cls, type_, name, shop):
        return cls.type[type_](name, shop)


class Shop:
    auto_id = 0

    def __init__(self, name):
        self.id = Shop.auto_id
        Shop.auto_id += 1
        self.name = name
        self.products = []

    def product_count(self):
        return len(self.products)


class Engine:
    def __init__(self):
        self.sellers = []
        self.buyers = []
        self.products = []
        self.shops = []

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_shop(name):
        return Shop(name)

    @staticmethod
    def create_product(type_, name, shop):
        return ProductFactory.create(type_, name, shop)

    def find_shop_by_id(self, id):
        for shop in self.shops:
            if shop.id == id:
                return shop
        raise KeyError(f"No shop with id: {id}")

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = decodestring(val_b)
        return val_decode_str.decode('UTF-8')


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls.__instances:
            return cls.__instances[cls]
        cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print(f"log: {text}")

from copy import deepcopy
from sqlite3 import connect
from quopri import decodestring
from project.patterns.behavioral_patterns import Subject, FileWriter
from project.patterns.architectural_system_pattern_unit_of_work import DomainObject


class User:
    def __init__(self, name):
        self.name = name


class Seller(User):
    pass


class Buyer(User, DomainObject):
    def __init__(self, name):
        self.products = []
        super().__init__(name)


class UserFactory:
    types = {
        'seller': Seller,
        'buyer': Buyer
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class ProductPrototype:

    def clone(self):
        return deepcopy(self)


class Product(ProductPrototype, Subject):

    def __init__(self, name, shop):
        self.shop = shop
        self.name = name
        self.shop.products.append(self)
        self.buyers = []
        super().__init__()

    def __getitem__(self, item):
        return self.buyers[item]

    def add_buyer(self, buyer):
        self.buyers.append(buyer)
        buyer.products.append(self)
        self.notify()


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
    def create_user(type_, name):
        return UserFactory.create(type_, name)

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

    def get_buyer(self, name):
        for buyer in self.buyers:
            if buyer.name == name:
                return buyer

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

    def __init__(self, name, writer=FileWriter()):
        self.writer = writer
        self.name = name

    def log(self, text):
        text = f"log: {text}"
        self.writer.write(text)


class BuyerMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.tablename = 'buyer'

    def all(self):
        statement = f'SELECT * FROM {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name = item
            buyer = Buyer(name)
            buyer.id = id
            result.append(buyer)
        return result

    def find_by_id(self, id):
        statement = f"SELECT id, name FROM {self.tablename} WHERE id=?"
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Buyer(*result)
        else:
            raise RecordNotFoundException(f'record with id={id} not found')

    def insert(self, obj):
        statement = f"INSERT INTO {self.tablename} (name) VALUES (?)"
        self.cursor.execute(statement, (obj.name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        statement = f"UPDATE FROM {self.tablename} SET name=? WHERE id=?"
        self.cursor.execute(statement, (obj.name, obj.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, obj):
        statement = f"DELETE FROM {self.tablename} WHERE id=?"
        self.cursor.execute(statement, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


connection = connect('patterns.sqlite')


class MapperRegistry:
    mappers = {
        'buyer': BuyerMapper
    }

    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, Buyer):
            return BuyerMapper(connection)

    @staticmethod
    def get_current_mapper(name):
        return MapperRegistry.mappers[name](connection)


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')

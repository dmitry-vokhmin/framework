class RegistryHolder(type):
    count = 0
    lst = []

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)

        '''
        <class '__main__.Animal'>
        <class '__main__.Bear'>
        <class '__main__.Cat'>
        class '__main__.Dog'>
        '''
        cls.count += 1
        cls.lst.append(new_cls.__name__)
        return new_cls


class Animal(metaclass=RegistryHolder):

    count = 0

    def __init__(self):
        Animal.count += 1


class Bear(Animal):
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


print(RegistryHolder.lst)

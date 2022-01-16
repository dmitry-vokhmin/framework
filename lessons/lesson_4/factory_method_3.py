from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def say(self):
        pass

    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            animal = Dog()
        elif animal_type == 'cat':
            animal = Cat()
        return animal


class Dog(Animal):

    def say(self):
        print('wow-wow')


class Cat(Animal):

    def say(self):
        print('мяу-мяу')

from factory_method_1 import Cat, Dog

animal_type = input()

if animal_type == 'dog':
    animal = Dog()
elif animal_type == 'cat':
    animal = Cat()

animal.say()

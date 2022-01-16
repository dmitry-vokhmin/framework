from factory_method_4 import Animal

animal_type = input()
animal = Animal.create_animal(animal_type)
animal.say()

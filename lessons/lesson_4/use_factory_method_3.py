from factory_method_3 import Animal

animal_type = input()
animal = Animal.create_animal(animal_type)
animal.say()

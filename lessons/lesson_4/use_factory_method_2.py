from factory_method_2 import AnimalCreator

animal_type = input()
animal = AnimalCreator.create_animal(animal_type)
animal.say()

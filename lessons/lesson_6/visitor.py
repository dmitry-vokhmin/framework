from abc import ABCMeta, abstractmethod


class Human(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class Programmer(Human):

    def accept(self, visitor):
        visitor.repair(self)


class Lawyer(Human):
    def accept(self, visitor):
        visitor.repair(self)


class ConstructionElementVisitor(metaclass=ABCMeta):

    @abstractmethod
    def repair(self):
        pass


class Cool(ConstructionElementVisitor):

    @abstractmethod
    def repair(self):
        print('Дорого', 'Круто')


class NotCool(ConstructionElementVisitor):

    @abstractmethod
    def repair(self):
        print('Дешево', 'Не Круто')

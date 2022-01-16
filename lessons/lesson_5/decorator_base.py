from abc import ABCMeta, abstractmethod


class Writer(metaclass=ABCMeta):
    @abstractmethod
    def write_message(self):
        pass


class ConcreteWriter(Writer):
    def write_message(self):
        print('writing message')


class WriterDecorator(Writer, metaclass=ABCMeta):
    def __init__(self, component):
        self._component = component

    @abstractmethod
    def write_message(self):
        pass


class CheckLengthDecorator(WriterDecorator):
    def write_message(self):
        print('checking message length')
        self._component.write_message()


class CompressDecorator(WriterDecorator):
    def write_message(self):
        print('compressing message')
        self._component.write_message()
        print('check compressed length')


concrete_writer = ConcreteWriter()
check_length_decorator = CheckLengthDecorator(concrete_writer)
compress_decorator = CompressDecorator(check_length_decorator)
compress_decorator.write_message()

"""
print('compressing message')
print('checking message length')
print('writing message')
print('check compressed length')
"""

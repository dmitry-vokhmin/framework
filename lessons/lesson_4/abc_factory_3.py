from abc import ABC, abstractmethod


# Семейство классов для VK
class VkParser:
    @staticmethod
    def parse():
        print('Vk parser work')


class VkAnalizer:
    pass


class VkSender:
    pass


# Семейство классов для одноклассников
class OdParser:
    @staticmethod
    def parse():
        print('Od parser work')


class OdAnalizer:
    pass


class OdSender:
    pass


# Семейство классов для твиттера
class TwParser:
    @staticmethod
    def parse():
        print('Tw parser work')


class TwAnalizer:
    pass


class TwSender:
    pass


class AbstractFactory(ABC):

    @staticmethod
    def create_factory(network_name):
        NETWORKS = {
            'Vk': VkFactory,
            'Od': OdFactory,
            'Tw': TwFactory
        }

        return NETWORKS[network_name]()

    @abstractmethod
    def create_parser(self):
        pass

    @abstractmethod
    def create_analizer(self):
        pass

    @abstractmethod
    def create_sender(self):
        pass


class VkFactory(AbstractFactory):
    def create_parser(self):
        return VkParser()

    def create_analizer(self):
        return VkAnalizer()

    def create_sender(self):
        return VkSender()


class OdFactory(AbstractFactory):
    def create_parser(self):
        return OdParser()

    def create_analizer(self):
        return OdAnalizer()

    def create_sender(self):
        return OdSender()


class TwFactory(AbstractFactory):
    def create_parser(self):
        return TwParser()

    def create_analizer(self):
        return TwAnalizer()

    def create_sender(self):
        return TwSender()

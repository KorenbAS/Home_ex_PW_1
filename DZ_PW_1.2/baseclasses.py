from abc import abstractmethod, ABC


class Abstract_reader(ABC):
    """ Абстрактний клас наслідники якого мають реалізовувати метод read() """
    @abstractmethod
    def read():
        pass


class Abstract_manager(ABC):
    """ Абстрактний клас наслідники якого мають реалізовувати метод interactive() """
    @abstractmethod
    def interactive():
        pass


class Abstract_view(ABC):
    """ Абстрактний клас наслідники якого мають реалізовувати метод draw() """
    @abstractmethod
    def draw():
        pass

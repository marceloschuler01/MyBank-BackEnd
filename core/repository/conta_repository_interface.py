import abc

class ContaRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def select_all(self):
        pass

    @abc.abstractmethod
    def select_by_id(self, id: int):
        pass

    @abc.abstractmethod
    def insert(self, conta):
        pass
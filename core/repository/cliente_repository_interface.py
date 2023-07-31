import abc

class ClienteRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def select_all(self):
        pass

    @abc.abstractmethod
    def select_by_id(self, id: int):
        pass

    @abc.abstractmethod
    def select_by_cpf(self, cpf: str):
        pass

    @abc.abstractmethod
    def insert(self, cliente):
        pass



        
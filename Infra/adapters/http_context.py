import abc

class HttpContext(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_request(self):
        pass

    @abc.abstractmethod
    def make_response(self, status:int, body:dict):
        pass
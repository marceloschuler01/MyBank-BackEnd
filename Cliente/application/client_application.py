from core.application.application import Application

class client_application(Application):
    def __init__(self, repository, id_cliente=None):
        super().__init__(repository=repository, id_client=id_cliente)


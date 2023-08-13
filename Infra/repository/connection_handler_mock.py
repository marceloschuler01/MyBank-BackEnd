from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from core.entity.agencia import Agencia
from core.entity.cliente import Cliente

class ConnectionHandlerMock():
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [
                        mock.call.query(Cliente),
                    ],
                    [Cliente(id=1, nome="Joao", cpf="123")]
                ),
                (
                    [
                        mock.call.get(Cliente, 1),
                    ],
                    [Cliente(id=1, nome="Joao", cpf="123")]
                ),
                (
                    [
                        mock.call.query(Agencia),
                    ],
                    [Agencia(id=1, nome="Trindade")]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
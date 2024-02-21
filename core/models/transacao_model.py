import datetime

class TransacaoModel:
    
    columns = {
        'id_conta_origem': {
            'required': True,
            'type': int,
            'unique': False,
        },
        'id_conta_destino': 
        {
            'required': True,
            'type': int,
            'unique': False,
        },
        'valor': 
        {
            'required': True,
            'type': float,
            'unique': False,
        },
        'data_transacao': {
            'required': True,
            'type': datetime.datetime,
            'unique': False,
        }
    }

    columns_to_define_unicity = [
    ]

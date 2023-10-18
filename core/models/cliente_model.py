COLUMNS = {
        'cpf': {
        'required': True,
        'type': str,
        'unique': True,
    },

        'nome': {
        'required': False,
        'type': str,
        'unique': False,
    },
        'data_nascimento': {
        'required': False,
        'type': str,
        'unique': False,
    },
        'email': {
        'required': False,
        'type': str,
        'unique': False,
    },
        'senha': {
        'required': True,
        'type': str,
        'unique': False,
    },
} 
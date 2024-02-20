class ContaModel:
    
    columns = {
        'id_cliente': {
            'required': True,
            'type': int,
            'unique': True,
        },
        'tipo': 
        {
            'required': False,
            'type': int,
            'unique': False,
        },
        'id_agencia': 
        {
            'required': False,
            'type': str,
            'unique': False,
        },
    }

    columns_to_define_unicity = [
        'id_cliente'
    ]

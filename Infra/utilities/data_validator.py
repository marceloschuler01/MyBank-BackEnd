class DataValidator:
    def __init__(self, model):
        self._model = model

    def validate(self, data: dict):
        for key, value in data.items():
            if not key in self._model.keys():
                return "Terrivel"
            if not isinstance(value, self._model[key]['type']):
                return "Tipo Invalido pelo amor de deus"

        for key in self._model:
            if self._model[key]['required']:
                if not key in data:
                    return f"Ai não po, faltou {key}"
        
        return "Valido"

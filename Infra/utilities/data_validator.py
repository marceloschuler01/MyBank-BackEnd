from Infra.exceptions.bad_request import BadRequest
from typing import cast

class DataValidator:
    def __init__(self, model):
        self._columns = model.columns
        self._not_found_keys = []
        self._invalid_type = []
        self._required_not_found_key = []
        self._validated_data = {}

    def validate(self, data: dict):
        for key, value in data.items():
            if not key in self._columns.keys():
                self._not_found_keys.append(key)
            else:
                self._cast_type(key, value)
        for key in self._columns:
            if self._columns[key]['required']:
                if not key in data:
                    self._required_not_found_key.append(key)

        if self._not_found_keys or self._invalid_type or self._required_not_found_key:
            invalid = {
                'validate_data': self._validated_data,
                'not_found_keys': self._not_found_keys,
                'invalid_type': self._invalid_type,
                'required_not_found_key': self._required_not_found_key,
                }
            raise BadRequest(message='Dados Inválidos', value=invalid)

        return self._validated_data

    def _cast_type(self, key, value):
        expected_type = self._columns[key]['type']
        try:
            result = cast(expected_type, value)
        except ValueError:
            self._invalid_type.append({key: {'expected type': str(expected_type), 'found': str(type(value))}})
        self._validated_data[key] = result

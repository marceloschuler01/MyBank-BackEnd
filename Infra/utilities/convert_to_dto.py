import dataclasses
from datetime import date, datetime

class ConvertToDTO:

    def __init__(self, dto):
        self._dto = dto
        self._entry: list | dto

    def convert(self, entry):
        self._entry = entry
        if isinstance(self._entry, list):
            return self.__convert_list_of_objects()
        return [self._convert_object(data=self._entry)]
    
    def __convert_list_of_objects(self):
        converted = []
        for data in self._entry:
            DTO = self._convert_object(data)
            converted.append(DTO)
        return converted

    def _convert_object(self, data):
        fields = dataclasses.fields(self._dto)
        kwargs = {}
        for field in fields:
            key = field.name
            value = getattr(data, key)
            if isinstance(value, datetime):
                kwargs[key] = value.strftime("%Y-%m-%d %H:%M:%S")
            elif type(value) in (int, str, float):
                kwargs[key] = value
            else:
                kwargs[key] = None
        dto = self._dto(**kwargs)
        return dto

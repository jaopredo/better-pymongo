from ..data_types import GeneralType
from pymongo.collection import Collection
from ..errors import InvalidDataPassed


class Meta(type):
    def __new__(mcs, name, bases, attrs):
        fields = {}
        for k, v in attrs.items():
            if "__" not in k and isinstance(attrs[k], GeneralType):
                fields[k] = v

        cls = type.__new__(mcs, name, bases, attrs)
        cls.fields = fields
        
        return cls


class Document(object, metaclass=Meta):
    class Configs:
        collection: Collection = None
    
    def save(self, data):
        collection = self.Configs.collection

        self.check(data)

        collection.insert_one(data)
    
    def check(self, data: dict):
        try:
            for k, v in data.items():
                self.fields[k].check_type(v)
        except KeyError as e:
            raise InvalidDataPassed(f"O dado {e.args[0]} não foi encontrado no Documento definido")

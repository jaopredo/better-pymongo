from ..data_types import GeneralType
from pymongo.collection import Collection
from ..errors import InvalidDataPassed
from ..utility.colors import Colors


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

        new_data = self.check(data)

        #collection.insert_one(new_data)
    
    def check(self, data: dict):
        # Checando se tem os mesmos campos
        for k, v in data.items():
            if k not in self.fields.keys():
                raise InvalidDataPassed(Colors.danger(f"The {k} field passed is not in the document fields"))
            
            

            self.fields[k].check_type(v)
            
            data[k] = self.fields[k].make_changes(v)

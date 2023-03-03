from abc import ABC, abstractmethod
from ..errors import *
from ..utility.colors import Colors

class GeneralType(ABC):
    """Classe abstrata para representar todos os tipos
    """
    def __init__(self, required=False, default=None, validate=None, immutable=False, unique=False):
        """Initianton of every GeneralType class

        Args:
            required (bool, optional): Tells if path is required. Defaults to False.
            default (_type_, optional): Tells a value if the path isn't passed. Defaults to None.
            validate (_type_, optional): Function that executes always before the path is saved. Defaults to None.
            immutable (bool, optional): Tells if the path can change. Defaults to False.
            unique (bool, optional): Tells if the path have to be the only one in all collection. Defaults to False.
        """
        self.required = required
        self.default = default
        self.validate = validate
        self.immutable = immutable
        self.unique = unique
        super().__init__()
    
    @abstractmethod
    def make_changes(self, value):
        return value

    @abstractmethod
    def check_type(self, data):
        pass


class NumberType(GeneralType):
    """Tipo numérico NÚMERO
    """
    def check_type(self, data):  # Função que checa o valor passado
        if not isinstance(data, int) and not isinstance(data, float):
            raise InvalidDataType(f"O dado {data} não foi reconhecido como numérico")
        return super().check_type(data)
    
    def make_changes(self, value):
        return super().make_changes(value)


class StringType(GeneralType):
    def __init__(self, required=False, default=None, validate=None, immutable=False, unique=False,
        lowercase: bool=False, uppercase: bool=False, trim: bool=True, enum: list=None, min_length: int=None, max_length: int=None
    ):
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.trim = trim
        self.enum = enum
        self.min_length = min_length
        self.max_length = max_length

        super().__init__(required, default, validate, immutable, unique)
    
    def check_type(self, data):
        if not isinstance(data, str):
            raise InvalidDataType(Colors.danger(f"O dado {data} não foi reconhecido como caracteres"))
        return super().check_type(data)
    
    def make_changes(self, value: str):
        if self.lowercase:
            value = value.lower()
        if self.uppercase:
            value = value.upper()
        if self.trim:
            value = value.strip()
        if self.min_length:
            if self.min_length > len(value):
                raise InvalidDataPassed(Colors.danger("The value is less than it could"))
        if self.max_length:
            if self.max_length < len(value):
                raise InvalidDataPassed(Colors.danger("The value is higher than it could"))
        if self.enum:
            if value not in self.enum:
                raise InvalidDataPassed(Colors.danger(f"The value {value} isn't in the possible values"))
        
        return super().make_changes(value)

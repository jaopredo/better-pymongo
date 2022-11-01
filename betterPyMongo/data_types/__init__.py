from abc import ABC, abstractmethod
from ..errors import *

class GeneralType(ABC):
    """Classe abstrata para representar todos os tipos
    """
    def __init__(self, required=False, default=None) -> None:
        super().__init__()

    @abstractmethod
    def check_type(self, data):
        pass


class NumberType(GeneralType):
    """Tipo numérico NÚMERO
    """
    def __init__(self, required=False, default=None) -> None:
        super().__init__(required, default)

    def check_type(self, data):  # Função que checa o valor passado
        if not isinstance(data, int) and not isinstance(data, float):
            raise InvalidDataType(f"O dado {data} não foi reconhecido como numérico")
        return super().check_type(data)


class StringType(GeneralType):
    def __init__(self, required=False, default=None) -> None:
        super().__init__(required, default)
    
    def check_type(self, data):
        if not isinstance(data, str):
            raise InvalidDataType(f"O dado {data} não foi reconhecido como caracteres")
        return super().check_type(data)
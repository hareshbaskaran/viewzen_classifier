from pandas import DataFrame
from abc import ABC, abstractmethod
from iris_classifier.utils.enums import ConnectionName
class Iconnector(ABC, abstractmethod):
    name : ConnectionName

    @abstractmethod
    def read(self) -> DataFrame:
        pass

## todo : TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases











import pandas as pd
from pydantic import model_validator
from ....utils.enums import ConnectionName
from ....utils.configs import DATASET_PATH
from .base_connector import Iconnector
class Localcsv(Iconnector):
    name : ConnectionName.csv

    @model_validator(mode="before")
    def validate(self) -> "Localcsv":
        if self.path is None:
            raise ValueError(
                "No Path has been provided"
            )
        return self

    def read(self):
        return pd.read_csv(DATASET_PATH)


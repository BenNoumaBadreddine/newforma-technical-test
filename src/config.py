from dataclasses import dataclass
import pandas as pd

# Define constant variables to ensure the maintainability of our code for others requirement,
# e.g: adding another int column
COLUMNS_CONVERT_TO_INT = ['backers']
COLUMNS_CONVERT_TO_FLOAT = ['goal', 'pledged', 'usd_pledged']
COLUMNS_CONVERT_TO_DATETIME = ['deadline', 'launched']
COLUMNS_TO_BE_DELETED = ['ID', 'name', 'launched', 'deadline', 'currency']
CATEGORICAL_COLUMNS_TO_ENCODE = ['category', 'main_category', 'country', 'state']

THEME_COLORS = ["#ff8533", "#808080"]

# Define a dictionary of exchange rates to USD
CURRENCY_EXCHANGE_RATES = {
    'GBP': 1.30,  # 1 GBP to USD
    'CAD': 0.75,  # 1 CAD to USD
    'NOK': 0.11,  # 1 NOK to USD
    'AUD': 0.72,  # 1 AUD to USD
    'EUR': 1.18,  # 1 EUR to USD
    'SEK': 0.11,  # 1 SEK to USD
    'NZD': 0.67,  # 1 NZD to USD
    'CHF': 1.08,  # 1 CHF to USD
    'DKK': 0.16,  # 1 DKK to USD
    'SGD': 0.74,  # 1 SGD to USD
    'HKD': 0.13,  # 1 HKD to USD
    'MXN': 0.050,  # 1 MXN to USD
    'USD': 1,
}


# define a column type converter class to handle the conversion of type column
@dataclass()
class ColumnTypeConverter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def convert_to_int(self, columns: list):
        self.df[columns] = self.df[columns].astype(int)

    def convert_to_float(self, columns: list):
        self.df[columns] = self.df[columns].astype(float)

    def convert_to_datetime(self, columns: list):
        self.df[columns] = self.df[columns].apply(pd.to_datetime)


@dataclass()
class StateValues:
    possible_states = ['undefined', 'successful', 'canceled', 'failed', 'suspended', 'live']
    valid_states = ['failed', 'successful']


@dataclass()
class MyColors:
    colors = ['blue', 'orange', 'black', 'red', 'green', 'cyan']

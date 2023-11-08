import pandas as pd
from category_encoders import BinaryEncoder
from config import CURRENCY_EXCHANGE_RATES
from currency_converter import CurrencyConverter

# Create a CurrencyConverter object with the provided exchange rates
converter = CurrencyConverter(CURRENCY_EXCHANGE_RATES)


# Function to convert 'goal' to USD
def convert_goal_to_usd(row):
    return converter.convert(row['goal'], row['currency'], 'USD')


def ordinal_encoding(df: pd.DataFrame, col_name: str, mapper: dict) -> pd.DataFrame:
    """
    Assigns numeric values to the col_name (ordinal variable). This technique is used for categorical variables where
    order matters
    :param df: The dataframe having the data
    :param col_name: The column col_name that will be filled by numeric values
    :param mapper: e.g mapper = {'very low': 1, 'medium low': 2, 'low': 3,
            'medium high': 4, 'high': 5, 'very high': 6,
            'unknown': 7}
    :return: dataframe with col_name having numeric values
    """
    # solution 1
    df[col_name].replace(mapper, inplace=True)
    # solution 2:
    # df[[col_name]] = df[[col_name]].apply(LabelEncoder().fit_transform)
    return df


def binary_encoding(df: pd.DataFrame, col_list: list) -> pd.DataFrame:
    """
    This function replace the categorical column or feature using the binary encoding technique.
     This technique is used for categorical variables where order does not matter
    :param df: The dataframe having the data
    :param col_list: The list of categorical columns
    :return:df: the dataframe with numeric column
    """
    # Initialize BinaryEncoder
    encoder = BinaryEncoder()
    transformed_df = encoder.fit_transform(df[col_list])
    df = pd.concat([df, transformed_df], axis=1)

    return df


def get_season_by_month(month: int) -> str:
    """
    This function returns the season of the year based on the month
    :param month: The month of the year as a number from 1 to 12
    :return: the season as a string
    """
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    else:
        return 'Invalid Month'

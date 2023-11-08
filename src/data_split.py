from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import pandas as pd


def dataframe_train_test_split(dataframe: pd.DataFrame, testing_percentage: float = 0.2) -> tuple[pd.DataFrame,
                                                                                                  pd.DataFrame]:
    """
    This function splits the dataframe into train and test subsets
    :param dataframe: the data as a dataframe
    :param testing_percentage: the percentage of the data in the testing set
    :return: train and test: two dataframes
    """
    # Set a fixed random seed for reproducibility
    random_seed = 99
    # Split the DataFrame into training and testing sets with shuffling
    train_df, test_df = train_test_split(dataframe, test_size=testing_percentage, random_state=random_seed)
    return train_df, test_df


def handle_unbalanced_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    This function deal with the un-balanced dataset.
    :param dataframe: The dataset as a dataframe structure
    :return: balanced_df: a balanced dataset
    """
    # Split the DataFrame into features (X) and the target variable (y)
    # First we extract the x Features and y Label
    X = dataframe.drop(['state'], axis=1)
    y = dataframe['state']

    # Create a SMOTE object
    smote = SMOTE(sampling_strategy='auto', random_state=42)

    # Apply SMOTE to the data
    balanced_df, y_resampled = smote.fit_resample(X, y)
    balanced_df['state'] = y_resampled

    return balanced_df


def dataset_balanced_split(dataframe: pd.DataFrame, testing_percentage: float = 0.2) -> tuple[pd.DataFrame,
                                                                                              pd.DataFrame]:
    """
    This function spits the data into train and test with taking into account having balanced dataset in both
    :param dataframe: The database as a dataframe structure
    :param testing_percentage: the percentage of the testing data
    :return: two dataframe representing the testing and training datasets
    """
    successful_df = dataframe[dataframe.state == 1]
    failed_df = dataframe[dataframe.state == 0]

    train_successful_df, test_successful_df = dataframe_train_test_split(successful_df, testing_percentage)
    train_failed_df, test_failed_df = dataframe_train_test_split(failed_df, testing_percentage)

    train_df = pd.concat([train_successful_df, train_failed_df], ignore_index=True)
    test_df = pd.concat([test_successful_df, test_failed_df], ignore_index=True)

    return train_df, test_df

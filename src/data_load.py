import pandas as pd


def load_data_from_csv(data_dir: str) -> pd.DataFrame:
    """
    This function load and prepare the data as a Dataframe structure
    :param data_dir: the directory to the csv file containing the data
    :return: df: a dataframe
    """
    n = 13
    df = pd.read_csv(data_dir, encoding='cp1252', usecols=[i for i in range(n)])
    df.rename(columns=lambda x: x.strip(), inplace=True)
    df.rename(columns={'usd pledged': 'usd_pledged'}, inplace=True)
    return df


def save_train_test_data(train_df: pd.DataFrame, test_df: pd.DataFrame):
    """
    this function saves the two dataframes representing the test and the train dataset
    :param train_df: the training dataset
    :param test_df: the testing dataset
    :return:
    """
    train_file_path = '../data/preprocessed_train_ks_dataset.csv'
    test_file_path = '../data/preprocessed_test_ks_dataset.csv'
    train_df.to_csv(train_file_path, index=False)
    test_df.to_csv(test_file_path, index=False)
    print('Preprocessed dataset saved correctly!')

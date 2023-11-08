import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import COLUMNS_CONVERT_TO_FLOAT, CATEGORICAL_COLUMNS_TO_ENCODE, \
    THEME_COLORS


def categorical_var_distribution(data: pd.DataFrame, column_name: str, number_of_bars: int = 0):
    """
    This function plots the categorical variable distribution
    :param data: a dataframe having the features and the records of the dataset
    :param column_name: The column name that we want to plot the distribution
    :param number_of_bars: it is a integer variable that allow us to visualize only the first n frequently
    used 'column_name' values. It is mainly for a better visualization and interpretation purposes
    :return: a graphic
    """
    if number_of_bars == 0:
        number_of_bars = data[column_name].nunique()
    fig, axes = plt.subplots(nrows=1, ncols=1)
    plt.rcParams["figure.figsize"] = (20, 3)

    ax = data[column_name].value_counts(normalize=True)[: number_of_bars].plot.bar(title='',
                                                                                   color=["#ff8533", "#808080"])
    ax.set_xlabel(column_name)
    ax.set_ylabel('Frequency')
    fig.set_size_inches(15, 8)
    fig.suptitle(f"{column_name} distribution", fontsize=13)


def numerical_var_distribution(dataframe: pd.DataFrame):
    """
    This function generates a report of analysis on each numerical variable
    :param dataframe: The original data to be analyzed
    :return: a graphic
    """
    for num_var in COLUMNS_CONVERT_TO_FLOAT:
        print(f"'{num_var}' distribution:")
        plt.figure(1)
        plt.subplot(121)
        sns.distplot(dataframe[num_var]);
        plt.subplot(122)
        dataframe[num_var].plot.box(figsize=(16, 5))
        plt.show()


def categorical_variables_versus_target(dataframe: pd.DataFrame, target: str):
    """

    :param dataframe:
    :param target:
    :return:
    """
    fig, axes = plt.subplots(nrows=2, ncols=2)
    variable_index = 0
    for i in range(2):
        for j in range(2):
            sns.countplot(data=dataframe, x=CATEGORICAL_COLUMNS_TO_ENCODE[variable_index], hue=target,
                          palette=THEME_COLORS, ax=axes[i, j])
            variable_index += 1

    fig.set_size_inches(15, 8)
    fig.suptitle("", fontsize=13)
    plt.show()

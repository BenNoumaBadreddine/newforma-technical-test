from sklearn.preprocessing import LabelEncoder

from cleaning_operations import is_valid_state
from config import ColumnTypeConverter, COLUMNS_CONVERT_TO_INT, COLUMNS_CONVERT_TO_FLOAT, COLUMNS_CONVERT_TO_DATETIME, \
    COLUMNS_TO_BE_DELETED, CATEGORICAL_COLUMNS_TO_ENCODE
from data_load import load_data_from_csv, save_train_test_data
from data_split import handle_unbalanced_dataset, dataset_balanced_split
from feature_engineering import convert_goal_to_usd, get_season_by_month, ordinal_encoding, binary_encoding



data_dir = "../data/ks_dataset.csv"
# load the data
df = load_data_from_csv(data_dir)
# filter the examples having successful or failed state
df = df[df.apply(is_valid_state, axis=1)]
# fill empty value of the column with zero. Anyway we are not going to use it for the ML model
df['usd_pledged'].fillna(0, inplace=True)

# Create an instance of the ColumnTypeConverter
converter = ColumnTypeConverter(df)
# Convert the columns to the specified data types
converter.convert_to_int(COLUMNS_CONVERT_TO_INT)
converter.convert_to_float(COLUMNS_CONVERT_TO_FLOAT)
converter.convert_to_datetime(COLUMNS_CONVERT_TO_DATETIME)

# Apply the function to the DataFrame
df['goal_usd'] = df.apply(convert_goal_to_usd, axis=1)
# create the derived feature :campaigns_duration
df['campaigns_duration'] = (df['deadline'] - df['launched']).dt.days
# create the derived features: day_launched, month_launched, year_launched, and week_day
df = df.assign(day_launched=df.launched.dt.day,
               month_launched=df.launched.dt.month,
               year_launched=df.launched.dt.year,
               week_day=df.launched.dt.weekday)
# create the derived feature: season
df['season'] = df['month_launched'].apply(get_season_by_month)

# Drop un-necessary columns
df.drop(columns=COLUMNS_TO_BE_DELETED, inplace=True)
# deal with the categorical variables
mapper = {'failed': 0, 'successful': 1}
df = ordinal_encoding(df, 'state', mapper)
categorical_cols = ['category', 'main_category', 'country', 'season']
df = binary_encoding(df, categorical_cols)
CATEGORICAL_COLUMNS_TO_ENCODE = CATEGORICAL_COLUMNS_TO_ENCODE + ['season']
df[CATEGORICAL_COLUMNS_TO_ENCODE] = df[CATEGORICAL_COLUMNS_TO_ENCODE].apply(LabelEncoder().fit_transform)

# handle the un-balanced data
balanced_df = handle_unbalanced_dataset(df)
# split the data for ML later use
train_df, test_df = dataset_balanced_split(balanced_df, testing_percentage=0.2)

# save the split data
# save_train_test_data(train_df, test_df)






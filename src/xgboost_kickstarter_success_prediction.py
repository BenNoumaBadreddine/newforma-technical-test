import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import pandas as pd


# load the data
train_df = pd.read_csv("../data/preprocessed_train_ks_dataset.csv")
test_df  = pd.read_csv("../data/preprocessed_test_ks_dataset.csv")

# choose the set of features
features = ['state', 'goal_usd', 'campaigns_duration',
                'day_launched', 'month_launched', 'year_launched', 'week_day', 'season',
               'category_0', 'category_1', 'category_2', 'category_3', 'category_4',
               'category_5', 'category_6', 'category_7', 'main_category_0',
               'main_category_1', 'main_category_2', 'main_category_3', 'country_0',
               'country_1', 'country_2', 'country_3', 'country_4']

# Define the training, testing inputs and labels
X_train = train_df[features].drop('state', axis=1)
y_train = train_df['state']
X_test = test_df[features].drop('state', axis=1)
y_test = test_df['state']

# Create the xgboost model and define the output to be probabilistic output
model = xgb.XGBClassifier(objective='binary:logistic')
# Train the model
model.fit(X_train, y_train)

# predict the test data using the trained model
y_pred_probabilities = model.predict_proba(X_test)[:, 1]

# evaluate the model
roc_auc = roc_auc_score(y_test, y_pred_probabilities)
accuracy = accuracy_score(y_test, (y_pred_probabilities > 0.5).astype(int))
print(f'ROC AUC: {roc_auc}')
print(f'Accuracy: {accuracy}')

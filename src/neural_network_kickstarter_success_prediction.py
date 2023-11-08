import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

train_df = pd.read_csv("../data/preprocessed_train_ks_dataset.csv")
test_df  = pd.read_csv("../data/preprocessed_test_ks_dataset.csv")


features = ['state', 'goal_usd', 'campaigns_duration',
                'day_launched', 'month_launched', 'year_launched', 'week_day', 'season',
               'category_0', 'category_1', 'category_2', 'category_3', 'category_4',
               'category_5', 'category_6', 'category_7', 'main_category_0',
               'main_category_1', 'main_category_2', 'main_category_3', 'country_0',
               'country_1', 'country_2', 'country_3', 'country_4']



X_train = train_df[features].drop('state', axis=1)
y_train = train_df['state']


X_test = test_df[features].drop('state', axis=1)
y_test = test_df['state']



# Create a neural network model
model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model
accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy[1]*100:.2f}%')

# Make predictions
predictions = model.predict(X_test)

# The 'predictions' variable now contains the probabilities for binary classification (class 1)

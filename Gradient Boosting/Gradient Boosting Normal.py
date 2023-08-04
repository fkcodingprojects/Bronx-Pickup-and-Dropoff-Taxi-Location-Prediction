#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import warnings
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from tqdm import tqdm

# Disable warning messages
warnings.filterwarnings("ignore")

# Load the merged_data file as a DataFrame
merged_data = pd.read_csv("merged_data.csv")

# Convert 'date' column to datetime type
merged_data['date'] = pd.to_datetime(merged_data['date'])

# Extract year, month, and day as separate features
merged_data['year'] = merged_data['date'].dt.year
merged_data['month'] = merged_data['date'].dt.month
merged_data['day'] = merged_data['date'].dt.day

# Split the data into training and testing sets
train_data = merged_data.loc[merged_data['date'].dt.year < 2019].copy()
test_data = merged_data.loc[merged_data['date'].dt.year == 2019].copy()

# Define the feature columns for preprocessing
categorical_features = ['hour', 'month', 'day']
numerical_features = ['trip_count', 'total_distance', 'total_fare', 'avg_trip_time', 'probability_trip',
                      'HourlyDryBulbTemperature', 'HourlyPrecipitation', 'HourlyRelativeHumidity', 'HourlyWindSpeed']

# Create preprocessing transformers for categorical and numerical features
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
numerical_transformer = StandardScaler()

# Combine the preprocessing transformers using ColumnTransformer
preprocessor = ColumnTransformer([
    ('categorical', categorical_transformer, categorical_features),
    ('numerical', numerical_transformer, numerical_features)
])

# Split training data into input features (X) and target variables (y)
X_train = train_data.drop(['PULocationID', 'DOLocationID'], axis=1)
y_train_pu = train_data['PULocationID']
y_train_do = train_data['DOLocationID']

# Preprocess the training data
X_train_preprocessed = preprocessor.fit_transform(X_train)

# Create Gradient Boosting model
model_pu = GradientBoostingClassifier(random_state=42)
model_do = GradientBoostingClassifier(random_state=42)

# Fit the models with the preprocessed training data with a progress bar
with tqdm(total=2) as pbar:
    model_pu.fit(X_train_preprocessed, y_train_pu)
    pbar.update(1)
    model_do.fit(X_train_preprocessed, y_train_do)
    pbar.update(1)

# Preprocess the testing data
X_test_preprocessed = preprocessor.transform(test_data.drop(['PULocationID', 'DOLocationID'], axis=1))

# Use the models to predict PULocationID and DOLocationID for 2019 data
pu_predictions = model_pu.predict(X_test_preprocessed)
do_predictions = model_do.predict(X_test_preprocessed)

# Create a DataFrame to store the predictions
predictions_df = pd.DataFrame({'PULocationID_pred': pu_predictions,
                               'DOLocationID_pred': do_predictions},
                              index=test_data.index)

# Concatenate the predictions DataFrame with the test_data DataFrame
test_data = pd.concat([test_data, predictions_df], axis=1)

# Define a function to check if PULocationID and DOLocationID match within the same hour and date
def check_match(row):
    match_pu = any((test_data['PULocationID'] == row['PULocationID_pred']) &
                   (test_data['hour'] == row['hour']) &
                   (test_data['date'] == row['date']))
    match_do = any((test_data['DOLocationID'] == row['DOLocationID_pred']) &
                   (test_data['hour'] == row['hour']) &
                   (test_data['date'] == row['date']))
    return match_pu and match_do

def check_pu_match(row):
    match_pu = any((test_data['PULocationID'] == row['PULocationID_pred']) &
                   (test_data['hour'] == row['hour']) &
                   (test_data['date'] == row['date']))
    return match_pu

def check_do_match(row):
    match_do = any((test_data['DOLocationID'] == row['DOLocationID_pred']) &
                   (test_data['hour'] == row['hour']) &
                   (test_data['date'] == row['date']))
    return match_do

# Calculate the accuracies
matching_pairs_count = sum(test_data.apply(check_match, axis=1))
pu_matching_pairs_count = sum(test_data.apply(check_pu_match, axis=1))
do_matching_pairs_count = sum(test_data.apply(check_do_match, axis=1))

percentage_matching_pairs = (matching_pairs_count / len(test_data)) * 100
pu_percentage_matching_pairs = (pu_matching_pairs_count / len(test_data)) * 100
do_percentage_matching_pairs = (do_matching_pairs_count / len(test_data)) * 100

print(f"Accuracy (Both PULocationID and DOLocationID match): {percentage_matching_pairs:.2f}%")
print(f"Accuracy (PULocationID matches): {pu_percentage_matching_pairs:.2f}%")
print(f"Accuracy (DOLocationID matches): {do_percentage_matching_pairs:.2f}%")


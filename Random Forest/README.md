# Random Forest Model Parameter Optimization

This repository contains code for optimizing the Random Forest model parameters to increase accuracy in predicting the Pickup Location (PULocationID) and Dropoff Location (DOLocationID) in taxi trip data.

## Data Source

The data used in this analysis is sourced from taxi trip records with additional features such as date, hour, trip count, total distance, total fare, average trip time, probability of a trip, and weather-related features like HourlyDryBulbTemperature, HourlyPrecipitation, HourlyRelativeHumidity, and HourlyWindSpeed.

## Model Parameter Optimization

To optimize the Random Forest model for improved accuracy, the following steps are performed:

1. Data Preprocessing: The dataset is split into training and testing sets, and the features are categorized as categorical and numerical.

2. Feature Preprocessing: Categorical features are one-hot encoded, and numerical features are standardized using StandardScaler.

3. Random Forest Model Creation: Two Random Forest models are created, one for predicting PULocationID and the other for predicting DOLocationID.

4. Hyperparameter Tuning: The model's hyperparameters are optimized using selected search.

5. Progress Bar: A progress bar is displayed to track the fitting progress of the Random Forest models.

6. Prediction and Accuracy Calculation: The optimized models are used to predict PULocationID and DOLocationID for the testing data. The accuracy of predictions is calculated based on whether both PULocationID and DOLocationID match within the same hour and date.

## Model Parameters

The Random Forest model parameters were fine-tuned to achieve the best possible accuracy. The optimized parameters are as follows:

- n_estimators
- criterion
- max_depth
- max_features
- max_leaf_nodes
- min_impurity_decrease
- min_samples_leaf
- min_samples_split

## Accuracy Results

After optimizing the model, the accuracy for matching both PULocationID and DOLocationID within the same hour and date is approximately XX%.

The accuracy for matching only PULocationID is approximately XX%.

The accuracy for matching only DOLocationID is approximately XX%.

These optimized Random Forest models can be utilized to make more accurate predictions on taxi trip data, helping in various transportation-related applications and analyses. Feel free to use this code as a reference to optimize Random Forest models for similar prediction tasks on your datasets.

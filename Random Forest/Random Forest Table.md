```python
import pandas as pd

# Read the CSV file into a DataFrame in Python
data = pd.read_csv("Random Forest Mod.csv")

# Convert "Results," "Difference," and "Percentage" columns to numeric
data["Results"] = pd.to_numeric(data["Results"])
data["Difference"] = pd.to_numeric(data["Difference"])
data["Percentage"] = pd.to_numeric(data["Percentage"])

# Create a DataFrame with the required columns
data_filtered = data[["Parameter", "Random.Forest", "Results", "Difference", "Percentage"]]

# Format the "Results," "Difference," and "Percentage" columns with one decimal place
data_filtered["Results"] = data_filtered["Results"].apply(lambda x: "{:.1f}".format(x))
data_filtered["Difference"] = data_filtered["Difference"].apply(lambda x: "{:.1f}".format(x))
data_filtered["Percentage"] = data_filtered["Percentage"].apply(lambda x: "{:.1f}".format(x))

# Print the DataFrame
print(data_filtered)
```

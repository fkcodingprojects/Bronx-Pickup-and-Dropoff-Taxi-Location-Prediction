#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from tabulate import tabulate
from IPython.display import display

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("Support Vector Machine Mod.csv")

# Convert "Results," "Difference," and "Percentage" columns to numeric
data["Results"] = pd.to_numeric(data["Results"])
data["Difference"] = pd.to_numeric(data["Difference"])
data["Percentage"] = pd.to_numeric(data["Percentage"])

# Format the "Results," "Difference," and "Percentage" columns with three significant figures
data["Results"] = data["Results"].apply(lambda x: "{:.1f}".format(x))
data["Difference"] = data["Difference"].apply(lambda x: "{:.1f}".format(x))
data["Percentage"] = data["Percentage"].apply(lambda x: "{:.1f}".format(x))

# Display the table using tabulate
table = tabulate(data[["Parameter", "Support.Vector.Machine", "Results", "Difference", "Percentage"]],
                 headers="keys", tablefmt="pipe", showindex=False)

print(table)


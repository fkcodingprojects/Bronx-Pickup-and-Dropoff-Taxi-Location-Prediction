```python
import pandas as pd
from flextable import FlexTable, set_table_properties, set_font, set_font_properties

# Read the CSV file into a DataFrame
data = pd.read_csv("Gradient Mod.csv")

# Convert "Results," "Difference," and "Percentage" columns to numeric
data["Results"] = pd.to_numeric(data["Results"])
data["Difference"] = pd.to_numeric(data["Difference"])
data["Percentage"] = pd.to_numeric(data["Percentage"])

# Create a flextable with all data
ft = FlexTable(data[["Parameter", "Gradient.Boosting", "Results", "Difference", "Percentage"]])

# Format the "Results," "Difference," and "Percentage" columns with three significant figures
ft.set_formatter("Results", format_str="{:.1f}")
ft.set_formatter("Difference", format_str="{:.1f}")
ft.set_formatter("Percentage", format_str="{:.1f}")

# Adjust column width to show the full length of "Parameter"
set_table_properties(
    ft,
    width = 2.5,
    part = "body",
    j = "Parameter"
)

# Add some styling to make the table look more professional
set_table_properties(ft, theme="theme_booktabs")  # Apply the booktabs theme
set_font_properties(ft, fontfamily="Arial")  # Change font to Arial
set_font_properties(ft, fontsize=10)  # Set font size to 10

# Print the flextable
print(ft)

```

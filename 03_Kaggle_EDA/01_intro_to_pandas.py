# First, we have to 'import' the library we just downloaded
import pandas as pd

# Let's create some raw data using a Dictionary
raw_data = {
    "House_Size_sqft": [1500, 2000, 1200, 2500],
    "Bedrooms": [3, 4, 2, 4],
    "Price_USD": [250000, 320000, 200000, 400000]
}

# Now, we use Pandas to turn that raw data into a clean Table (DataFrame)
housing_table = pd.DataFrame(raw_data)

print("--- Real Estate Data ---")
print(housing_table)
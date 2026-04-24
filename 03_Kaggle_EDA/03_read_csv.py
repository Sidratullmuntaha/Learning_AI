import pandas as pd

# 1. Load the data from the CSV file into a Pandas DataFrame
print("Loading data...")
housing_data = pd.read_csv("03_Kaggle_EDA/pakistan_real_estate.csv")

# 2. Print the first 5 rows of the data
print("\n--- Top 5 Rows of the Dataset ---")
print(housing_data.head())

# 3. Print a quick mathematical summary of the data
print("\n--- Data Summary ---")
print(housing_data.describe())

housing_data1=pd.DataFrame(housing_data)
print(housing_data1)
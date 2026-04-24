import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle  # <-- Make sure this is at the top!

# 1. Load the data
housing_data = pd.read_csv("03_Kaggle_EDA/pakistan_real_estate.csv")

# 2. Prepare the Features (X) and the Target (y)
X = housing_data[["Size_sqft", "Bedrooms"]] 
y = housing_data["Price_USD"]

# 3. Create the AI Model
print("Creating the AI model...")
model = LinearRegression()

# 4. Train the Model
model.fit(X, y)
print("Model trained successfully!")

# 5. Make a prediction for a brand new house
new_house = pd.DataFrame({"Size_sqft": [1600], "Bedrooms": [3]})
predicted_price = model.predict(new_house)

print("\n--- AI Prediction ---")
print("Predicted price for a 1600 sqft, 3-bedroom house: $", int(predicted_price[0]))

# 6. THE MISSING PIECE: Save the trained model to a file
with open("05_Machine_Learning/real_estate_model.pkl", "wb") as file:
    pickle.dump(model, file)
print("\nModel saved successfully as real_estate_model.pkl!")
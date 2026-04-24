from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import pandas as pd

# 1. Start the API
app = FastAPI()

# 2. Load the trained AI model (Wake up the Chef!)
# 'rb' means 'read binary' because it's a special pickled file, not regular text.
with open("05_Machine_Learning/real_estate_model.pkl", "rb") as file:
    ai_model = pickle.load(file)

# 3. Define the Menu (What information must the customer provide?)
# We use 'BaseModel' to ensure the user gives us exactly what the AI needs.
class HouseOrder(BaseModel):
    Size_sqft: int
    Bedrooms: int

# 4. The Front Page Route
@app.get("/")
def read_root():
    return {"message": "Welcome to Sidra's AI Server!"}

# 5. NEW: The Prediction Route (Where the customer places their order)
# We use @app.post instead of .get because the user is POSTING data to us.
@app.post("/predict")
def predict_price(order: HouseOrder):
    
    # Take the customer's order and format it for the AI
    data = pd.DataFrame([{"Size_sqft": order.Size_sqft, "Bedrooms": order.Bedrooms}])
    
    # Ask the AI for the prediction
    prediction = ai_model.predict(data)
    
    # Bring the final bill back to the customer
    return {"estimated_price_usd": int(prediction[0])}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
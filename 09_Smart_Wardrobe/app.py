from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ==========================================
# 1. THE SCHEMA (How the AI sees clothes)
# ==========================================
class ClothingItem(BaseModel):
    id: int
    name: str
    category: str    # "top", "bottom", "shoes", "outerwear"
    color: str
    formality: str   # "casual", "smart-casual", "formal"
    season: str      # "summer", "winter", "all"

# ==========================================
# 2. THE DIGITAL WARDROBE (Mock Database)
# ==========================================
my_wardrobe = [
    {"id": 1, "name": "White Cotton T-Shirt", "category": "top", "color": "white", "formality": "casual", "season": "summer"},
    {"id": 2, "name": "Navy Blue Jeans", "category": "bottom", "color": "blue", "formality": "casual", "season": "all"},
    {"id": 3, "name": "Charcoal Suit Pants", "category": "bottom", "color": "grey", "formality": "formal", "season": "all"},
    {"id": 4, "name": "Crisp White Button-Down", "category": "top", "color": "white", "formality": "formal", "season": "all"},
    {"id": 5, "name": "Black Leather Oxford Shoes", "category": "shoes", "color": "black", "formality": "formal", "season": "all"},
    {"id": 6, "name": "White Sneakers", "category": "shoes", "color": "white", "formality": "casual", "season": "all"},
    {"id": 7, "name": "Heavy Wool Peacoat", "category": "outerwear", "color": "navy", "formality": "smart-casual", "season": "winter"}
]

# ==========================================
# 3. THE RULE-BASED ENGINE (The Stylist)
# ==========================================
@app.get("/recommend")
def get_outfit_recommendation(target_formality: str, current_season: str):
    
    recommended_outfit = {
        "top": None,
        "bottom": None,
        "shoes": None,
        "outerwear": None
    }
    
    # Rule 1: Filter the database for items that match the user's needs
    for item in my_wardrobe:
        
        # Only look at clothes that match the event type and weather
        is_right_event = (item["formality"] == target_formality) or (item["formality"] == "smart-casual")
        is_right_weather = (item["season"] == current_season) or (item["season"] == "all")
        
        if is_right_event and is_right_weather:
            # Slot the item into the correct part of the outfit
            if item["category"] == "top" and recommended_outfit["top"] is None:
                recommended_outfit["top"] = item["name"]
            
            elif item["category"] == "bottom" and recommended_outfit["bottom"] is None:
                recommended_outfit["bottom"] = item["name"]
                
            elif item["category"] == "shoes" and recommended_outfit["shoes"] is None:
                recommended_outfit["shoes"] = item["name"]
                
            elif item["category"] == "outerwear" and recommended_outfit["outerwear"] is None:
                recommended_outfit["outerwear"] = item["name"]

    return {"event_type": target_formality, "weather": current_season, "suggested_outfit": recommended_outfit}
# ==========================================
# 4. ADD NEW CLOTHES (User Input)
# ==========================================
@app.post("/add_item")
def add_clothing_item(new_item: ClothingItem):
    
    # Convert the user's data into a dictionary and add it to our mock database
    my_wardrobe.append(new_item.model_dump())
    
    return {
        "message": f"Successfully added {new_item.name} to your wardrobe!", 
        "total_items": len(my_wardrobe)
    }
# To run: uvicorn 09_Smart_Wardrobe.app:app --reload
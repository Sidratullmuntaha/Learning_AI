# Creating a list of tech brands (using square brackets)
tech_brands = ["Apple", "Samsung", "Google", "Sony"]

# Printing the entire list
print("All brands:", tech_brands)

# Printing just the FIRST item in the list
# IMPORTANT: In programming, we always start counting from 0, not 1!
print("The first brand is:", tech_brands[0])

# Printing the SECOND item
print("The second brand is:", tech_brands[1])




# --- DICTIONARIES ---
# A dictionary uses curly braces {} and assigns a Value to a Key using a colon.

my_profile = {
    "name": "Sidra",
    "role": "AI Developer",
    "modules_completed": 1
}

# Instead of using a number like [0], we just ask for the Key we want!
print("Developer Name:", my_profile["name"])
print("Modules Done:", my_profile["modules_completed"])
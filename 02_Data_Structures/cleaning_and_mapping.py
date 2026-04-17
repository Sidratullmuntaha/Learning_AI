# A list containing multiple dictionaries
developers = [
    {"name": "Sidra", "role": "Beginner"},
    {"name": "Ali", "role": "Intermediate"},
    {"name": "Sara", "role": "Senior"}
]

print("--- Data Update in Progress ---")

# We use a loop to look at each developer's dictionary one by one
for dev in developers:
    
    # Let's manipulate the data: We are upgrading everyone's role!
    dev["role"] = "Senior AI Developer"
    
    # Print out the mapped result
    print(dev["name"] + " is officially a " + dev["role"] + "!")
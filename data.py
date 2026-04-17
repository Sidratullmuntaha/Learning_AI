# 1. Writing data to a new file
with open("secret_data.txt", "w") as file:
    file.write("Sidra is becoming a Full-Stack AI Developer!")

# 2. Reading the data back out
with open("secret_data.txt", "r") as file:
    saved_text = file.read()
    
# 3. Manipulating the text (making it ALL CAPS)
shouting_text = saved_text.upper()
print(shouting_text)
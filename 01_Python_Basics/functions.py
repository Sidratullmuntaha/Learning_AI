# 1. Defining a function (Writing the recipe)
# We are creating a function that takes one ingredient: 'name'
def greet_developer(name):
    print("Hello " + name + ", you are crushing Module 1!")

# 2. Calling the function (Using the recipe)
greet_developer("Sidra")
greet_developer("Huzai134") # A shoutout to your friend's GitHub!

# 3. A function that calculates something and hands back a result (returns)
def calculate_cost(price, quantity):
    total = price * quantity
    return total  # The 'return' keyword hands the final answer back to us

# We call the math function, and store the returned answer in a new variable
my_final_bill = calculate_cost(4.50, 3)
print("The final bill is: $", my_final_bill)
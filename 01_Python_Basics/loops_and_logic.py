# 1. If/Else Statements (Making Decisions)
coffee_price = 4.50
my_wallet = 3.00

print("--- Decision Making ---")
if my_wallet >= coffee_price:
    print("Action: Buying coffee!")
else:
    print("Action: Not enough money, making tea at home instead.")

# 2. For Loops (Repeating Tasks)
print("\n--- Looping ---")
# The 'range(1, 6)' function tells Python to count from 1 up to, but NOT including, 6.
for module_number in range(1, 6):
    print("Currently working on Module:", module_number)
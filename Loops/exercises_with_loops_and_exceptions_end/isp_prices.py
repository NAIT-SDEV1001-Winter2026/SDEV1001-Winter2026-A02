package = input("Enter the package: ").upper()
hours = 0
try:
    hours = int(input("Enter the number of hours used: "))
except ValueError:
    print("Please enter a valid number of hours")

PACKAGE_A_PRICE = 9.95
PACKAGE_A_VARIABLE_PRICE = 2.00
PACKAGE_B_PRICE = 13.95
PACKAGE_B_VARIABLE_PRICE = 1.00
PACKAGE_C_PRICE = 19.95

total_price = 0

if package == "A":
    total_price += PACKAGE_A_PRICE
elif package == "B":
    total_price += PACKAGE_B_PRICE
elif package == "C":
    total_price += PACKAGE_C_PRICE


for hour in range(hours):
    if package == "A":
        if hour >= 10:
            total_price += PACKAGE_A_VARIABLE_PRICE
    elif package == "B":
        if hour >= 20:
            total_price += PACKAGE_B_VARIABLE_PRICE

print(f"The total price is ${total_price}")

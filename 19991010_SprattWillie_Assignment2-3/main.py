# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Write your assignment statements here for profit, salePrice, and saleProfit


# the "profit" variable will hold the variable "retailPrice" minus the variable "wholesalePrice"

profit = retailPrice - wholesalePrice

# the "salePrice" variable will hold the variable "retailPrice" minus the same variable "retailPrice" multiplied by 0.25 to mimic 25% off within parenthesis

salePrice = retailPrice - (retailPrice * 0.25)

# the "saleProfit" variable will hold variable "salePrice" minus the variable "wholesalePrice"

saleProfit = salePrice - wholesalePrice


print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))

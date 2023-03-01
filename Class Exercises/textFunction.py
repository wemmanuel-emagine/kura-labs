from functools import total_ordering
import time

meatBill = 0
sidesBill = 0
drinksBill = 0
total_Bill = 0

# Functions

menu = {"Meat": ["Jerk Chicken", "Sweet & Sour Chicken", "BBQ Wings", "Curry Goat", "Curry Chicken", "Smoked Lamb", "Lobster Based in Butter", ],
        "Sides": ["Mac & Cheese", "Rice", "Plantin", "Greenfig Salad", "Mash Potatos", "Bake Potatos", "Salad"],
        "Drinks": ["Tequila Sunrise", "Martini", "White Russian", "Long Island Ice Tea", "My Fair Lady", "Sex On The Beach", "Water"]
        }


def menuMeat(meatInput):
    global meatBill
    print(meatBill)
    print(meatInput)
    if meatInput == ("Curry Chicken" or "Sweet & Sour Chicken" or "BBQ Wings"):
        meatBill += 55
        print(meatBill)
        print(meatInput)
    elif meatInput == ("Jerk Chicken" or "Curry Goat" or "Smoked Lamb"):
        meatBill += 50
        print(meatBill)
    else:
        meatBill += 100
        print(meatBill)


def menuSides(sidesInput):
    global sidesBill
    print(sidesBill)
    if sidesInput == ("Mac & Cheese" or "Bake Potatos" or "Greenfig Salad"):
        sidesBill += 45
        print(sidesBill)
    elif sidesInput == ("Rice" or "Plantin" or "Mash Potatos"):
        sidesBill += 35
        print(sidesBill)
    else:
        sidesBill += 25
        print(sidesBill)


def menuDrinks(drinkInput):
    global drinksBill
    print(drinksBill)
    if drinkInput == ("Tequila Sunrise" or "Martini" or "White Russian"):
        drinksBill += 20
        print(drinksBill)
    elif drinkInput == ("White Russian" or "Long Island Ice Tea" or "My Fair Lady" or "Sex On The Beach"):
        drinksBill += 18
        print(drinksBill)
    else:
        drinksBill += 0
        print(drinksBill)


print(f"They proceed to sit at a table and the waiter gives them the menu...")
print("The menu include:\n")
print("Meat:")
for key in menu["Meat"]:
    print(key)
print("")
time.sleep(1)
meatInput = input("Then the waiter askes what meat are you having:")
menuMeat(meatInput)
time.sleep(1)
print("Sides:")
for key in menu["Sides"]:
    print(key)
print("")
time.sleep(1)
sidesInput = input("Then the waiter askes what sides are you having:")
menuSides(sidesInput)
time.sleep(1)
print("Drinks:")
for key in menu["Drinks"]:
    print(key)
print("")
time.sleep(1)
drinksInput = input("Then the waiter askes what drinks are you having:")
menuDrinks(drinksInput)
time.sleep(1)

print(meatBill)
print(sidesBill)
print(drinksBill)

total_Bill = meatBill + sidesBill + drinksBill
print(total_Bill)

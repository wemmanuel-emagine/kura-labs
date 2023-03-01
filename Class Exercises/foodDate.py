#!/bin/python3

# Importation of Libraries
import time
import os

# to center the First Print Statement
width = os.get_terminal_size().columns

# Variables for each person and a Variable for the restaurant
person1 = "Bonnie"
person2 = "Clyde"
restaurant = "The Assassination Corner"

# List for your rating and Dictionary for your menu
rating = ["Boring","Ok","Great"]
menu = {"Meat": ["Jerk Chicken", "Sweet & Sour Chicken", "BBQ Wings", "Curry Goat", "Curry Chicken", "Smoked Lamb", "Lobster Based in Butter", ],
        "Sides": ["Mac & Cheese", "Rice", "Plantin", "Greenfig Salad", "Mash Potatos", "Bake Potatos", "Salad"],
        "Drinks": ["Tequila Sunrise", "Martini", "White Russian", "Long Island Ice Tea", "My Fair Lady", "Sex On The Beach", "Water"]
        }
total_Bill = 0
meatBill = 0
sidesBill = 0
drinksBill = 0

# Functions

def menuMeat(meatInput):
    global meatBill
    if meatInput == ("Curry Chicken" or "Sweet & Sour Chicken" or "BBQ Wings"):
        meatBill += 25
        print(meatBill)
    elif meatInput == ("Jerk Chicken" or "Curry Goat" or "Smoked Lamb"):
        meatBill += 50
        print(meatBill)
    else:
        meatBill += 100
        print(meatBill)


def menuSides(sidesInput):
    global sidesBill
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
    if drinkInput == ("Tequila Sunrise" or "Martini" or "White Russian"):
        drinksBill += 20
        print(drinksBill)
    elif drinkInput == ("White Russian" or "Long Island Ice Tea" or "My Fair Lady" or "Sex On The Beach"):
        drinksBill += 18
        print(drinksBill)
    else:
        drinksBill += 0
        print(drinksBill)


def total_bill():
        global total_Bill
        global meatBill
        global sidesBill
        global drinksBill
        global wallet
        
        total_Bill = (meatBill + sidesBill + drinksBill)*2
        wallet-=total_Bill 

def ratingOption(ratingInput):
    global wallet
    if ratingInput == "Boring" and str(wallet <=200) :
        print("Your date didn't go well....\nYou wont get a second date")
    elif ratingInput == "OK" and str(wallet <=400) :
        print("Your date didn't go well....\nBut....\nYou might get her number")
    elif ratingInput == "Great" and str(wallet >=600) :
        print("Your date went well....\nYour gonna get a second date for sure....")


print("=============================================================================================================================".center(width))
print("The Story of the Assassination Corner.........".center(width))
print("=============================================================================================================================".center(width))
time.sleep(3)
print(f"{person1} and {person2} went to {restaurant} to have a lovely lunch date.\n")
time.sleep(1)
print(f"When they walked in, the waiter greeted them and asked:")
time.sleep(1)
# Getting the User Input for the wallet variable
wallet = int(input(
    f"Welcome to {restaurant}, as protocal I need to ask how much money do you have currently: "))
time.sleep(2)
print(f"While {person1} looked into his wallet, he saw that he had ${wallet}\n")
time.sleep(1)
# if the person has less then 100
if wallet < 330:
    print(f"The Waiter tells {person1} that he doesn't have enough money.... ")
    time.sleep(1)
    print(f"{person1} is furious but {person2} calms him down and told him that he shouldn't make a scene since there are too many people around.")
    time.sleep(1)
    print(f"{person1} sighs and revaluating the situation he leaves with {person2}..")
    time.sleep(3)
else:
    print(f"The waiter told them that they have enough money to dine at the restaurant and lets them in.")
    time.sleep(1)
    print(f"They proceed to sit at a table and the waiter gives them the menu...")
    print("The menu include:\n")
    print("Meat:")
    # Print every thing in the meat list
    for key in menu["Meat"]:
        print(key)
    print("")
    time.sleep(1)
    # Asking for the user input for meat input
    meatInput = input("Then the waiter askes what meat are you having: ")
    menuMeat(meatInput)
    time.sleep(1)
    print("")
    print("Sides:")
    #Print everything in the sides list
    for key in menu["Sides"]:
        print(key)
    print("")
    time.sleep(1)
    # Ask the user for the input for the sides
    sidesInput = input("Then the waiter askes what sides are you having: ")
    menuSides(sidesInput)
    time.sleep(1)
    print("")
    print("Drinks:")
    # Print everything for the drinks list
    for key in menu["Drinks"]:
        print(key)
    print("")
    time.sleep(1)
    # ask for the input for the drinks
    drinksInput = input("Then the waiter askes what drinks are you having: ")
    menuDrinks(drinksInput)
    time.sleep(3)
    print("")
    print(f"So after {person1} and {person2} had their meal, the waiter came with the bill....")
    total_bill()
    print(f"Your total bill is ${total_Bill}")
    print(f"{person1} has ${wallet} in his wallet\n")
    time.sleep(1)
    # Get the rating input
    for key in rating:
        print(key)
    print("")
    ratingInput = input("From the rating above, how would you describe your date: ")
    ratingOption(ratingInput)
    


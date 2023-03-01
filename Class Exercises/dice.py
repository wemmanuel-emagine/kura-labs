# Examples of Creating classes and objects
import random

class Dice:
    def __init__(self,name,color,sides):
        self.name = name
        self.color = color
        self.sides = sides
        print(f"You made a dice named:{self.name}, and gave it a color:{self.sides}")
   

    # Making DiceRoll Function
    def diceRoll(self):
        roll = random.randint(1,self.sides)
        # print that shows dice name color and roll value
        print(f"Your Dice named {self.name}, rolled a valued of {roll}")



# ---------Class End-----------------#

# Creating 2 Dice objects using the class
myDice = Dice("Lucky","red",6)
myOtherDice = Dice("BadLuck","Blue",13)

# Running the DiceRoll function on the object
myDice.diceRoll()
print(myDice.name)
print(myOtherDice.color)
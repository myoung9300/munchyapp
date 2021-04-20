'''
munchy! App 3.0
By Myoung
The pourpose if this app is to provide a meal planner for the week and an ingreadience
list to go shopping for the meals
'''
#  ------- Github --------

pip install -r requirements.txt
setup.py

#  ------- Imports --------

from random import choice
import time


#  -------- A Functions -----------
   #A1 Chooose Dishes

def meals(days):
    time.sleep(2)
    while len(MunchMenu) < int(days):
        meal = choice(MealList)
        if meal not in MunchMenu:
            MunchMenu.append(meal)
    print("DONE... Here is your Menus for the week...")
    time.sleep(1)
    print()
    for meal in MunchMenu:   #INPUT DAYS OF WEEK HERE...
        print(meal)
    print()
    print("Out of all these dishes, my favorite has to be " + choice(MunchMenu))
    print()
    print("Would you like to see a shopping list?")
    slanswer = input("Please type yes or no? ")

    if slanswer == 'y' or slanswer == 'Y' or slanswer == 'yes' or slanswer == 'YES':
        buildShoppingList()
        print()
        time.sleep(2)
        print("I really hope you enjoy these meals that I have chosen for you! Good Bye...")
    else:
        print("Hopefully you have all of the ingredients for the dishes that I have chosen for you...  GOOD BYE")


   #A2 Build shopping list

def buildShoppingList():
    print()
    print("OK. Give me a sec to put the list together...")
    time.sleep(3)
    print()
    print("Here you go...")
    
    ShoppingList = []
    if "Spagetti" in MunchMenu:
        ShoppingList.append(Spagetti)
    if "Pork Chops" in MunchMenu:
        ShoppingList.append(PorkChops)
    if "Hot Dogs & Hamburgers" in MunchMenu:
        ShoppingList.append(HotDogsHamburgers)
    if "Steak" in MunchMenu:
        ShoppingList.append(Steak)
    if "BBQ Chicken" in MunchMenu:
        ShoppingList.append(BBQchicken)
    if "Chicken Alfrado" in MunchMenu:
        ShoppingList.append(ChickenAlfrado)
    if "Salmon" in MunchMenu:
        ShoppingList.append(Salmon)
    if "Chicken Tenders & Mac-n-Cheese" in MunchMenu:
        ShoppingList.append(ChickenTenders)
    if "Chili" in MunchMenu:
        ShoppingList.append(Chili)
    if "Bacon Pasta" in MunchMenu:
        ShoppingList.append(BaconPasta)
    if "Tacos" in MunchMenu:
        ShoppingList.append(Tacos)
    if "Breakfast Burritos" in MunchMenu:
        ShoppingList.append(BreakFastBurritos)
    if "Street Tacos" in MunchMenu:
        ShoppingList.append(StreetTacos)

    print()
    for meal in ShoppingList:
        print()
        for ing in meal:
            print(ing)

#A3 Build going out list

def GoingOut():
    Out = []
    option = choice(OutList)
    if option not in Out:
        Out.append(option)
        print()
        print("OK... I have Chosen for you ...")
        print()
        time.sleep(2)
    for option in Out:
        print(option)
        print()
        time.sleep(1)
        print("Enjoy!!")

    

#  -------- B Lists  ------------

MealList = ["Spagetti" , "Pork Chops" , "Hot Dogs & Hamburgers" , "Steak" , "BBQ Chicken" , "Chicken Alfrado" , "Salmon" , "Chicken Tenders & Mac-n-Cheese" , "Chili" , "Bacon Pasta" , "Tacos" , "Breakfast Burritos" , "Street Tacos"]

MunchMenu = []

Spagetti = ["Spagetti" , "Sauce" , "Garlic Bread" , "Sausage" , "Salad"]
PorkChops = ["Pork Chops" , "Potatos" , "Asparagus"]
HotDogsHamburgers = ["Hot Dogs" , "Hamburgers" , "Bratwurst" , "Buns" , "American Cheese" , "chips" , "Cottage Cheese"]
Steak = ["Steak" , "broccoli" , "Velveeta Cheese" , "Potatos"]
BBQchicken = ["Chicken" , "BBQ Sauce" , "Salad" , "Asparagus"]
ChickenAlfrado = ["Chicken" , "Noodles" , "Alfrado Sauce" , "Salad", "Garlic Bread"]
Salmon = ["Salmon" , "Potatos" , "Salad"]
ChickenTenders = ["Chicken Strips" , "Mac-N-Cheese" , "French Fries"]
Chili = ["2 cans of Chili Beans" , "1 can of Kidney Beans" , "1 can of Rotel Orginal" , "2 cans of Diced Tomatos (Orgenano,Basil,&Garlic)" , "1 can of tomato soup" , "Ground Beef" , "Cheese" , "Fritos" , "Sour Cream"]
BaconPasta = ["Baccon" , "Pasta" , "Potato Salad"]
Tacos = ["Gound Beef" , "Mexican Seasoning" , "Small Tortillas" , "Sour Cream" , "Tomato" , "Lettuce" , "Guac" , "Cheese"]
BreakFastBurritos = ["Breakfast Sausage" , "Hash Browns" , "Large Tortillas" , "Eggs" , "Mild Chili" , "Hot Chili"]
StreetTacos = ["Gound Beef" , "Mexican Seasoning" , "Corn Tortillas" , "Sour Cream" , "Tomato" , "Lettuce" , "Guac" , "Cheese" , "Oil (If we don't have any)"]


OutList = ["Chilis'" , "Chick-Fil-A" , "McDonald's" , "Subway" , "Q-Doba" , "Chipotle" , "Wendy's" , "Taco Bell"]


#1 How many days to plan?

print("Hello!!")
time.sleep(1)
print("My name is MUNCHY! I will help you figure out what to eat...")
time.sleep(1)
print("I have a few questions for you...")
time.sleep(1)
print("Would you like to go out for dinner or would you like to make food from home?")
outanswer = input("Type OUT - going out or IN - Making food at home... ")
if outanswer == 'O' or outanswer == 'o' or outanswer == 'out' or outanswer == 'OUT':
    GoingOut()
else:
    answer = input("How many days would you like me to plan for? ")
    print("OK... I'm going to plan for " + answer + " Dinner(s) from my meals list")

#2 Choose dishes...

    meals(answer)


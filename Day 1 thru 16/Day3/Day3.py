# Day 3 Conditional Statements, Logical Operations Code Blocks and Scope Namespacing
#
# #===================If Else Statement
# if condition:
#     do this
# elif:
#     do this
# print ("Welcome to the roller coster ride")
# height = int(input ("How tall are you? "))
# if height > 120:
#     print("You can ride the ride")
# elif height != 119 or height < 118:
#     print("Mkae magic happen")
# else
#     print("You can not ride the ride")

# #================== Modulo Operator exercise
# modulo = 10 % 3
# num_entred = int(input("Enter a odd or even integer: "))
# if num_entred % 2 == 0:
#     print ("You entered " + str(num_entred)+". This is an even number.")
# else:
#     print ("You entered " + str(num_entred)+". This is an odd number.")

#================== Nested If/else
# print ("Welcome to the roller coster ride")
# height = int(input ("How tall are you? "))
# age = int(input ("How old are you? "))
#
# if height > 120:
#     print("You can ride the ride")
#     if age < 12 :
#         print ("You owe $5.")
#     elif age >= 12 & age < 18 :
#         print ("You owe $7.")
#     else:
#         print ("You owe $12.")
# else:
#     print("You can not ride the ride")

#================== BMI Calculator with Interpretations
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi < 18.5:
#     print ("underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print ("normal weight")
# else:
#     print ("overweight")
#===========================
# print ("Welcome to the Pizza Place!")
# size = input ("What size pizza do you want? S, M, L: ")
# pepperoni = input ("Do you want pepperoni? Y, N: ")
# extra_cheese = input ("Do you want extra cheese? Y or N:  ")
# pizza_price = round(float(0), 2)
# if size.lower() == "s":
#     pizza_price = 15.00
#     if pepperoni.lower() == "y": pizza_price +=2.00
# elif size.lower() == "m":
#     pizza_price = 20.00
#     if pepperoni.lower() == "y": pizza_price +=3.00
# elif size.lower() == "l":
#     pizza_price = 25.00
#     if pepperoni.lower() == "y": pizza_price +=3.00
# if extra_cheese.lower() == "y":
#     pizza_price += 1.00
#
# print (f"Your total pizza is: ${pizza_price}")
#
# print(False or True or False)
#===================Logical Operators
## Learnt about and or not operators
#===================================
# Final Project
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input ("You're at a cross road. Where do you want to go? \n Type \"left\" or \"right\" ")
lake = ""
door = ""

if cross_road == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. \n Type \"wait\" to wait for the boat. Type \"swim\" to swim across.")
    if lake == "wait":
        door = input ("Which door would you like to go? \n Type \"red\" or \"yellow\" or \"blue\"")
        if door == "yellow":
            print ("You won!")
if cross_road == "right" or lake != "wait" or door != "yellow":
    print("Game Over")



#===================Print Function: Output text to console
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.\n4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#===================Input function: Collect data from User
input("What is your name? ")

#===================Function Nesting With Print and Input
print("Hello "+ input ("What is your name") + "!")

#===================Variables
name = input("What is your name? ")
print ("Your name is " + name)

#===================Functions - Length (len) and String (str)
print ("Your name, is "+ str(len(input("What is your name? ")))+" characters in length")


#===================Functions - Length (len) and String (str) with Variable
username = input("What is your name? ")
length = len(username)
print ("Your name, is "+ str(length) +" characters in length")

#===================Variable Swap Challenge
# Challenge: Swap the contents of two variables (glass1 and glass2)
# glass1 contains milk, and glass2 contains juice.
# You are not allowed to type the words "milk" or "juice" in your code.
# Use only variables and complete the swap in 3 lines.
glass1 = "milk"
glass2 = "juice"
glass3 = glass1
glass1 = glass2
glass2 = glass3
print ("glass 1:" + glass1 + "  glass2: "+glass2)

#===================The inportance of variablenameing and commenting to remember the name of the variable. Python uses snake_case naming convention


#===================Band Name Generator with function Capitalize
print("Welcome to the Band Name Generator!")
print("What is the name of the city you grew up in? ")
city_name = input()
print("What is your pet's name? ")
pet_name = input()
print("Your band name could be "+ city_name.capitalize() + " " + pet_name.capitalize())

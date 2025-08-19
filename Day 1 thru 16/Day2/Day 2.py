# Day 2 Focuses on Data Types, Numbers, Operators, Type Conversion, f-Strings and more
#
# #===================Data Types- String ans Subscripting
# string_type = "This is a string"
# print (string_type[6]) #Subscripting is extracting parts of a string using the index of the String
# print (string_type[-2]) #Negative numbers also helps to extract starting from the last number of a string
# #===================Data Types- Integer
# stest = int("1")
# largeIntegers = 123_443_432 # rather than , to seperate large numbers use _
# #===================Data Types- Float
# float_data = 3.45
# #===================Data Types- Boolean
# boolean = "True"
# boolean = bool(boolean)
#
#
# #===================Fixing integer in length function
# fix_length_function = len(str(12345))
#
# #===================Type Function
# float(fix_length_function)
# print (type(float_data))
# print (type(fix_length_function))
# print (type("11111"))
# print (type(boolean))
#
#
# #===================Fix the TypeError Challenge
# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# #===================Implecit type casting
# print (5/3)
# print (5//3) #cast without floaing numbers
# print(2**2) # raised to the power of 2
#
#
# #=================== BMI Calculator
# height = 1.65
# weight = 84
# bmi = (weight / (height ** 2))
# print (bmi)
#
# #=================== Rounding function & flooring
# print (int(bmi)) #returns the floor of a float
# print (round(bmi)) #returns the ceiling
# print (round(bmi,3))# of a float
#
# #=================== Assignment Operator
# score = 0
# score +=1
#
# #=================== f strings allows users to combine things that have diffrent data types
# print (f"Your score is {score} your height is {height} cm. and your bmi is {bmi} cm.")

# #=================== Tip Calculator
print ("Welcome to the tip calculator!")
total_bill = input ("What was the total bill? $")
tip = input ("How much tip would you like to gift (10, 12, or 15)? ")
number_of_people = input ("How many people will be splitting the bill? ")
bill_plus_tip = float(total_bill) + (float(total_bill) * (float(tip) / float(100)))
bill_per_person = round((bill_plus_tip / float(number_of_people)),2)

print (f"Each person should pay ${bill_per_person}")



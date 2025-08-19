#============== Debuging
    #6 tips to debugging code
#========================== 1) Describe the problem
def my_function():
    for i in range(1,20): #Code loops from 0 - 19
        if i==20:
            print("You got it")
my_function()

#========================== 2) Reproduce a Bug
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 6)
# dice_num = 6 #Reproduce the error
# print(dice_images[dice_num])

#========================== 3) Play Computer
# Trace the code by hand with a few inputs.
# Example 1: year = 1993
#   1980 < 1993 < 1994  -> True  -> prints "You are a millennial."
# Example 2: year = 1994
#   1980 < 1994 < 1994  -> False
#   1994 > 1994         -> False -> prints nothing (boundary bug).
# Example 3: year = 2001
#   1980 < 2001 < 1994  -> False
#   2001 > 1994         -> True  -> prints "You are a Gen Z."
# This hand-tracing reveals that 1994 and any year <= 1980 produce no output.
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994: #Line by line wa
    print("You are a Gen Z.")

#========================== 4) Fix the Error
age = int(input("How old are you?"))
#if age > 18:
#print("You can drive at age {age}.")

# ========================== 5) Use print()
# Use print to walk through your code to catch bugs

# ========================== 6) Use Debugger










































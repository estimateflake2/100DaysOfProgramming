#================== Functions with input (parameter) - Final project - Ceaser Cipher
# In Python, a function with input (also called a parameter) is a reusable block of code
# that accepts values when called. These values (arguments) allow the function to perform
# its task dynamically based on the provided input.
#
# This project uses functions with input to implement the Caesar Cipher, an encryption technique.
# A cipher is a method of transforming readable text (plaintext) into an unreadable form (ciphertext)
# to protect its meaning. The Caesar Cipher is a substitution cipher where each letter in the
# message is shifted by a fixed number of positions in the alphabet.
#
# It is called the Caesar Cipher because Julius Caesar famously used it to protect military messages
# by shifting letters a set number of spaces, making them unreadable without knowing the shift key.
#========================================== Variable Initialization
#=======================================================================================
#================== Functions
# def greet():
#     print (f"Hello World")
#     print ("Welcome to Python")
#     print (f"Make it a great day!")
# greet()

#================== Functions with Parameter
# Parameters vs Arguments:
# - A parameter is a variable listed inside the parentheses in a function definition.
#   It acts as a placeholder for the value the function will receive when called.
#
# - An argument is the actual value you pass to the function when you call it.
#   This value gets assigned to the corresponding parameter inside the function.
#
# Example:
# def greet(name):     # 'name' is the parameter
#     print(f"Hello, {name}!")
#
# greet("Alice")       # "Alice" is the argument
#=======================================================================================

# def greet(str):
#     print (f"Hello {str}")
#     print ("Welcome to Python")
#     print (f"Make it a great day {str}!")
# greet(input ("\n\nWhat is your name? ").capitalize())

#================== Life in Weeks Exercise
# def life_in_weeks(age):
#     num_weeks_in_year = 52
#     weeks_left = (90 - age) * num_weeks_in_year
#     print (f"You have {weeks_left} weeks left.")
# print ("Ready to find out how weeks till you turn 90?")
# age = int(input("What is your age? "))
# life_in_weeks(age)
#=======================================================================================

#================== Furnction with Multiple input
# def greet_with(name, location):
#     print (f"Hello, {name}")
#     print (f"What is it like in {location}?")
# n = str(input("What is your name? "))
# loc = str(input("What is location? "))
# greet_with(n, loc)
#=======================================================================================

#================== Love Calculator Exercise
# def calculate_love_score(name1, name2):
#     love_score = 0
#     combined = (name1 + name2).replace(" ","").lower()
#     true_word = "true"
#     love_word = "love"
#     def true_occurance(word):
#         counter = 0
#         for letter in "true":
#             for l in word:
#                 if l == letter:
#                     counter += 1
#         return counter
#     def love_occurance(word):
#         counter = 0
#         for letter in "love":
#             for l in word:
#                 if l == letter:
#                     counter += 1
#         return counter
#
#     print(str(true_occurance(combined))+ str(love_occurance(combined)))
# calculate_love_score("Kanye West", "Kim Kardashian")
# calculate_love_score("Angela Yu", "Jack Bauer")
#=======================================================================================

#================== Caesar_cipher
from caesar_cipher import caesar_cipher_1
cyfr = caesar_cipher_1
print(cyfr.logo)
ext = False
while not ext:
     usr_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
     if usr_input == "encode":
         usr_message = input("Type your message: ")
         usr_shift_num = int(input("Type the shift number: "))
         encoded_message = cyfr.czr_encode(usr_message, usr_shift_num)
         print(f"Here is your encrypted message: {encoded_message}")
         usr_proceed = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
         if usr_proceed == "no": ext = True

     elif usr_input == "decode":
         usr_message = input("Type your message: ")
         usr_shift_num = int(input("Type the shift number: "))
         decoded_message = cyfr.czr_decode(usr_message, usr_shift_num)
         print(f"Here is your decoded result: {decoded_message}")
         usr_proceed = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
         if usr_proceed == "no": ext = True
     else:
         ext = True








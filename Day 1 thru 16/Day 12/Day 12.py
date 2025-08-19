#========================================== Number Guessing Project
#======Scope
# Scope: The "scope" of a variable is where in the program that variable can be used.
# Variables made inside a function can only be used in that function (local scope).
# Variables made outside all functions can be used anywhere in the file (global scope).

# enemies = 1 #global scope
# def increase_enemies():
#     enemies = 2 #local scope
#     print(f"local enemies inside function: {enemies}")
# increase_enemies()
# print(f"global enemies: {enemies}")

#===== There is no Block Scope in Python, unlike java
# Variables created inside if/for/while blocks are still accessible outside the block.
# Only functions (and some special cases like comprehensions) create their own scope.
# In Java, variables declared inside { } cannot be accessed outside those braces,
# but in Python, the variable still exists in the surrounding function or global scope.

#================== Coding Exercise = Prime Number Checker
# def is_prime(num):
#     """returns true if a number is prime and false otherwise"""
#     local_var = True
#     if num <= 1:
#         local_var = False
#     for n in range (2,num):
#         if num % n == 0:
#             local_var = False
#     return local_var
# print(is_prime(21))

#================== Modifying Global scope within a function
# It is generally not a good idea to modify a global scope within a function
# It is also not a good idea to call a local variable the same name as a global scope
# enemies = 1 #global scope
# def increase_enemies():
#     global enemies  #local scope
#     enemies = 10
#     print(f"local enemies inside function: {enemies}")
# increase_enemies()
# print(f"global enemies: {enemies}")

#================== Global Constants
# It is good practise to define global scope as all caps
# PI = 3.14159

#========================================== Final Project
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
print (logo)
print ("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
play_game = True
computer_num = random.randint(1,100)
def check_value (value):
    value_match = False
    if value < computer_num:
        print("Too low.")
    elif value > computer_num:
        print("Too high.")
    else:
        print(f"You got it! The answer was {value}")
        value_match = True
    return value_match

def ask_user (attempts):
    counter = 0
    while counter < attempts:
        print(f"You have {attempts - counter} attempts remaining to guess the number")
        usr_value = int(input("Make a guess: "))
        if not check_value (usr_value):
            counter +=1
        else:
            break
    if counter == attempts:
        print("You've run out of guesses, you lose.")

while play_game:
    difficulty = str(input ("Choose a difficulty. Type 'exit', 'easy' or 'hard': "))
    if difficulty == "easy":
        ask_user(10)
    elif difficulty == "hard":
        ask_user(5)
    else:
        play_game = False













































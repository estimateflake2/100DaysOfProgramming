#================== For Loops, Range, Code Blocks
#================== For Loop
# fruits = ["Apple", "Peach", "Pear"]
# for index, fruit in enumerate (fruits):
#     print(f"The fruit of today is {fruit}. It is the {index+1} fruit in the array")
#================== Exercise Use forloop to replicate the MAX function
# def add_array(data):
#     value = 0
#     for dat in data:
#         if (dat>value):
#             value = dat
#     return value
# student_score = [150,1,43,1200,344,134,553,23,45]
# print (f"Max of given array is {add_array(student_score)}")

#================== Using Loops Independently
# for n in range (100): print(n)
# print ("===========================")
# for n in range (1, 10): print(n) #Domain range
# print ("===========================")
# for n in range (1, 10, 2): print(n) #Domain range with Steps
#================== Carl Friedrich Gauss Challenge
# ans =0
# for n in range (101):
#     ans +=n
# print (ans)
#================== Fizz Buzz Challenge
# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)
#================== Final Project: PyPassword Generator!
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ltrs = []
sym = []
numb = []
for i in range(nr_letters):
    ltrs.append(random.choice(letters))
for i in range(nr_symbols):
        sym.append(random.choice(symbols))
for i in range(nr_numbers):
    numb.append(random.choice(numbers))
#     print(ltrs)
#
#
# print ("ltrs ", ltrs)
# print ("sym ", sym)
# print ("numb ", numb)

password_chars = ltrs + sym + numb
# print(password_chars)
random.shuffle(password_chars)
# print(password_chars)
usr_password = "".join(password_chars)
print(f"Your password is: {usr_password}")
















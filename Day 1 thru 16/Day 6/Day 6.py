#================== Functions, Code Blocks, and While Loops  ==================#
#================== Functions
# functions are accompanied by ()
def my_function():
    x =0
    return x
print (my_function())

#================== Code Blocks
# In Python, indentation is used to define blocks of code.
# Functions, loops, and conditionals must be indented properly to work.
def my_function():
    x =0
    return x
if my_function() == 0:
    print(my_function())
    if my_function() % 2 == 0:
        print(f"my_function() is {my_function()}")

#================== While Loop
# A while loop runs as long as a condition is True.
# It's useful when you don't know ahead of time how many times the loop should run.
# You need to manually manage the condition inside the loop (e.g., updating a counter).

# This is different from a for loop, which runs a set number of times or through each item in a list.
# For loops are better when you're working with a known sequence (like a list or a range).
a = 0
while 1==1:
    print (a)
    a +=1
    if a >= 10:
        break





















#========================================== Day 10 Functions with Output. Final Project Calculator App
# A function with output returns a value when it is called.
# Instead of just performing an action (like printing), it sends data back to the caller,
# allowing you to store it in a variable or use it in further calculations.
# Example:
# def add(a, b):
#     return a + b
# result = add(5, 3)  # result will be 8

# def format_name(f_name, l_name, case):
#     if case=="title":
#         return f_name.title()," ",l_name.title()
#     return  l_name.capitalize()+", "+f_name.capitalize()
# print(format_name(input("Enter the first name: "), input("Enter the second name: "),"title"))
# print(format_name(input("Enter the first name: "), input("Enter the second name: "),"not title"))

#============= Coding Excersise - Leap Year Checker
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
print (is_leap_year(2020))

#============= Doc Strings: A way to create documentation as we write a code
def is_leap_year(year):
    """This method checks if a year is leap year.
        It takes a given year and returns True if the year is a leap year and False otherwise""" #A docstring goes after the start of a method
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
print (is_leap_year(2020))






















#========================== Object Oriented Programming (OOP)
# Marks the start of a section that demonstrates Object Oriented Programming (OOP) concepts,
# such as classes, objects, and methods.
#===================Note
# Things to consider when modelling an Object (1) What it Has [attributes=>variables], (2) What it does [method]
# Objects are instances of a Class
# Methods are functions in an Object
# Classes are written in PascalCase in python
# A package is a group of Class available for use

##########################################################################################
#Programming Requirements:
    # TODO 1) Needs to be able to tell what resources are remaining.
    # TODO 2) Check for resource availability (sufficiency) when a user orders a drink
    # TODO 3) Must be able to process coins
    # TODO 4) Must be able to check for successful transaction
    # TODO 5) Make coffee
    # TODO 6) Has a secret "off" command to turn the machine off
##########################################################################################

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
c_m = CoffeeMaker()
m_m = MoneyMachine()
power = "on"
while power != "off":
    usr_input = input (f"What would you like? ({m.get_items()}report): ")
    if usr_input == "report":
        c_m.report()
        m_m.report()
    elif usr_input in ["expresso","latte","cappuccino"]:
        drink = m.find_drink(usr_input)
        if drink and c_m.is_resource_sufficient(drink):
            if m_m.make_payment(drink.cost):
                c_m.make_coffee(drink)
    elif usr_input == "off":
        break
    else:
        print ("invalid input. Please try again.")
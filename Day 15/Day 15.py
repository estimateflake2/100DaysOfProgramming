#========================== Virtual Coffee Machine
# This program simulates a coin-operated coffee machine.
# It manages limited resources (water, milk, coffee), processes user coin input,
# checks if resources and payment are sufficient, and dispenses one of three drinks
# (Espresso, Latte, Cappuccino). It also includes a hidden "off" command to stop the machine.

#1) Make 3 Hot Flavors
    #Expresso ($1.50): #50 ml Water #18g Coffee
    #Latte ($2.50): #200ml Water #24g Coffee #150ml Milk
    #Cappuccino ($3.00): #250ml Water #24g Coffee #100ml Milk

    #The Coffee Machine has the following resources to Manage:
        #300ml of water, 200ml of milk, 100g of coffee
#Coint Operated:
    #Penny (1 cent), Nickel (5 cents), Dime (10 cents), Quarter (25 cents)

#Programming Requirements:
    # TODO 1) Needs to be able to tell what resources are remaining.
    # TODO 2) Check for resource availability (sufficiency) when a user orders a drink
    # TODO 3) Must be able to process coins
    # TODO 4) Must be able to check for successful transaction
    # TODO 5) Make coffee
    # TODO 6) Has a secret "off" command to turn the machine off
##########################################################################################
import coffe_lib as data

def print_aval_resource ():
    """
    Prints the current status of the coffee machine’s resources and money.

    - Loops through available resources (water, milk, coffee)
      and displays each with its quantity and unit.
    - Shows the total money collected, converted from cents to dollars.
    """
    resource = data.resources
    money = data.money
    for i in resource:
            print(f"{i}: {resource[i]["quant"]}{resource[i]["unit"]}")
    print (f"Money: ${money["money"]/100}")

def check_resource_avail(user_request):
    """
    Checks if the coffee machine has enough resources to make the requested drink.

    Process:
    - Looks up the drink in the menu.
    - Compares the required ingredients against the current available resources.
    - If any ingredient is insufficient, prints a message (e.g., "Sorry there is not enough milk.")
      and returns False.
    - If the drink does not exist in the menu, notifies the user and returns False.
    - Returns True if all required resources are available.
    """
    menu = data.MENU
    resources = data.resources
    item_found = False
    missing_resources = []
    for i in menu:
        if i == user_request:
            item_found = True
            for ingredient in menu[i]["ingredients"]:
                if  menu[i]["ingredients"][ingredient] > resources[ingredient]["quant"]:
                    print (f"Sorry there is not enough {ingredient}.")
                    return False
    if not item_found:
        print ("Sorry, that option is not available. Please try again")
        return False
    return True

def check_sufficient_transaction(user_money, user_request):
    """
    Verifies if the user has inserted enough money to purchase the selected drink.

    Process:
    - Looks up the cost of the requested drink from the menu.
    - Compares the user's inserted money against the drink's cost.
    - If the money is insufficient:
        - Prints a message notifying the user and refunding the amount.
        - Returns False to indicate the transaction failed.
    - Returns True if the user has enough money for the purchase.
    """
    menu = data.MENU
    if menu[user_request]["cost"]>user_money:
        print (f"Sorry that's not enough money. ${menu[user_request]["cost"]/100} Is required. Money refunded: ${user_money/100}")
        return False
    elif menu[user_request]["cost"]<user_money:
        change = user_money - menu[user_request]["cost"]
        data.money["money"] += user_money - change
        print (f"Here is ${change/100} in change")
    else:
        print ("No change required")
    return True

def collect_and_process_coin(user_request):
    """
    Handles the coin input process for purchasing a drink.

    Process:
    - Prompts the user to input the number of quarters, dimes, nickels, and pennies.
    - Converts the total coin input into cents and calculates the user's total money.
    - Calls `check_sufficient_transaction()` to verify if the user has inserted enough money
      for the selected drink.
    - If insufficient, returns False to indicate the transaction cannot proceed.
    - Returns True if the user has provided enough money to complete the transaction.
    """
    # Penny (1 cent), Nickel (5 cents), Dime (10 cents), Quarter (25 cents)
    quarters = float(input ("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    user_money = float(quarters*25 + dimes*10 + nickles*5 + pennies)
    if not check_sufficient_transaction(user_money, user_request):
        return False
    return True

def make_coffee(user_request):
    """
    Handles the process of making coffee based on the user's request.

    This function first checks if there are enough resources available
    to make the requested drink. If resources are sufficient, it then
    collects and processes the user's coin input to ensure the
    transaction is successful. Only if both conditions are met does
    the function proceed to 'make' the coffee.

    Returns:
        bool: True if the coffee can be successfully made
              (resources available and transaction successful),
              otherwise False.
    """
    if check_resource_avail(user_request):
        if collect_and_process_coin(user_request):
            return True
    return False
power = "on"
while power != "off":
    usr_input = input ("What would you like? (expresso/latte/cappuccino/{report}: ")
    if usr_input == "report":
        print_aval_resource()
    elif usr_input in ["expresso","latte","cappuccino"]:
        make_coffee(usr_input)
    elif usr_input == "off":
        break
    else:
        print ("invalid input. Please try again.")

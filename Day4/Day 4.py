#================== Randomisation and Python Lists
# ===Python uses the Mersenne Twister number generator to randomly generate number

#================== Using the Random class
import random

#================== Using provate Class
# import my_module
#
# rand_int = random.randint(1,100) ## Random Integer within a given range
# rand_float = random.random() ## floating random between 0 and 1
# rand_large_float = random.uniform(1,2)
#
# for i in range(100):
#     rand_int = random.randint(1,100)
#     print(rand_int)
#     print (my_module.my_fav_num)
#     print(random.random())
#     print(rand_large_float)

#================== Practics Task - Choice head or tail
# user_input = input('Heads or Tails pick one (h or t): ')
# randAns = random.random()
# response = "Tails (t)"
# if randAns > 0.5 :
#     response = "Heads (h)"
# if user_input == "h" and randAns > 0.5 :
#     print( f"You Won {response} it is {randAns}")
# elif user_input == "t" and randAns <= 0.5 :
#     print( f"You Won {response} it is")
# else:
#     print (f"you lose! ")

#================== List
# fruits = ["apple", "banana", "cherry", "orange", "strawberry","pear","banana","onion"]
# fruits.append("pinanable")
# for index, fruit in enumerate(fruits):
#     print(index, " : ", fruit)
# print(random.choice(fruits))

#======================= Randomized Bill Pay
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(f"Today {random.choice(friends)} pays the bill.")
# hint = random.randint(0, len(friends)-1)
# print (f"Tomorrow {friends[hint]} pays the bill.")
#
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
#======================= Rock scissors Paper
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
for i in range (3):
    avail_choices = [rock, paper, scissors]
    choice = input ("Select Rock, Paper, or Scissors (R,P,S): ")
    computer_choice = random.choice(avail_choices)
    if choice == "R":
        if computer_choice == avail_choices[1]:
            print(f"You lose! The computer chose Paper: {computer_choice}")
        elif computer_choice == avail_choices[2]:
            print(f"You win! The computer chose Scissors: {computer_choice}")
        else:
            print(f"Draw! Try again. The computer chose Rock: {computer_choice}")

    elif choice == "P":
        if computer_choice == avail_choices[2]:
            print(f"You lose! The computer chose Scissors: {computer_choice}")
        elif computer_choice == avail_choices[0]:
            print(f"You win! The computer chose Rock: {computer_choice}")
        else:
            print(f"Draw! Try again. The computer chose Paper: {computer_choice}")

    elif choice == "S":
        if computer_choice == avail_choices[0]:
            print(f"You lose! The computer chose Rock: {computer_choice}")
        elif computer_choice == avail_choices[1]:
            print(f"You win! The computer chose Paper: {computer_choice}")
        else:
            print(f"Draw! Try again. The computer chose Scissors: {computer_choice}")

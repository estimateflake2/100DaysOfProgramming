#========================================== Day 10 Blackjack Capstone Project
# ACE is either 1 or 11 (user decides which value they want their Ace to represent
# Jack, Queen and King count as 10
# all other numeric cards count as their face value
import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print (logo)
stack = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
         "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 12,
         "King": 13,"Ace": [1,11]
         }
user_deck = []
computer_deck = []
def random_card_selector(agent):
    """Given an agent - computer (c) or user (u), this function returns a random card."""
    card = random.choice(list(stack.keys()))
    if card == "Ace":
        if agent == "c":
            value = random.choice([1, 11])
        else :
            value =0
            while not value == 1 and value != 11:
                value = int(input ("Ace was selected, do you want 1 or 11? "))
    else:
        value = stack.pop(card)
    return {card: value}
def encrypt_card (comp_deck):
    """Given a deck of cards, encrypt the last number in the card."""
    encrypted_card = []
    for i, card in enumerate(comp_deck):
        if i == len(comp_deck) - 1:
            encrypted_card.append("*")
        else:
            encrypted_card.append(card)
    return encrypted_card
def total (card_list):
    """Given a list of cards, this function returns the total number of cards."""
    total = 0
    for card in card_list:
        total += card
    return total
def check_game_over(usr_deck, cmp_deck, usr_select_end):
    """Given a list of cards, this function checks if the game is over. If the computer or user's deck is over 21, then they lose"""
    print(f"Your cards: {usr_deck}, current score: {total(usr_deck)}")
    print(f"Computer's card(s): {encrypt_card(cmp_deck)} ")
    if total (usr_deck) == 21 and total (cmp_deck) == 21:
        print(f"\n========================================================")
        print(f"Your cards: {usr_deck}, current score: {total(usr_deck)}")
        print(f"Computer's card(s): {cmp_deck} ")
        print("Draw 🙃")
        print(f"========================================================\n")
        return 'n'
    elif total (usr_deck) > 21 >= total (cmp_deck):
        print(f"\n========================================================")
        print(f"Your cards: {usr_deck}, current score: {total(usr_deck)}")
        print(f"Computer's card(s): {cmp_deck} ")
        print("You went over. You lose 😭")
        print(f"========================================================\n")
        return 'n'
    elif total (cmp_deck) > 21 >= total (usr_deck):
        print(f"\n========================================================")
        print(f"Your cards: {usr_deck}, current score: {total(usr_deck)}")
        print(f"Computer's card(s): {cmp_deck} ")
        print("Opponent went over. You win 😁")
        print(f"========================================================\n")
        return 'n'
    elif usr_select_end == 'y' and total (usr_deck) > total (cmp_deck):
        print(f"\n========================================================")
        print(f"Your cards: {usr_deck}, current score: {total(usr_deck)}")
        print(f"Computer's card(s): {cmp_deck} ")
        print("You win 😃")
        print(f"========================================================\n")
        return 'n'
    elif usr_select_end == 'y' and total (usr_deck) < total (cmp_deck):
        print(f"\n========================================================")
        print(f"Your cards: {usr_deck}, current score: {total(usr_deck)}")
        print(f"Computer's card(s): {cmp_deck} ")
        print("You lose 😤")
        print(f"========================================================\n")
        return 'n'
    elif usr_select_end == 'y' and total (usr_deck) == total (cmp_deck):
        print(f"\n========================================================")
        print(f"Your cards: {usr_deck}, current score: {total(usr_deck)}")
        print(f"Computer's card(s): {cmp_deck} ")
        print("Draw 🙃")
        print(f"========================================================\n")
        return 'n'
    return 'y'
while True:
    start_game = input ("\nDo you want to play a game of Blackjack? Type 'y' or 'n':")
    if start_game == "n":
        print("Thank you for playing")
        break
    elif not start_game == "n" and not start_game == "y":
        print("Invalid input. Please type 'y' or 'n':")
    elif start_game == "y":
        user_deck.append(list(random_card_selector("u").values())[0])
        user_deck.append(list(random_card_selector("u").values())[0])
        computer_deck.append(list(random_card_selector("c").values())[0])
        computer_deck.append(list(random_card_selector("c").values())[0])
        continue_game = check_game_over(user_deck, computer_deck, "n")
        while continue_game == 'y':
            continue_game = input ("\nType 'y' to get another card, type 'n' to pass: ")
            if continue_game=='y':
                user_deck.append(list(random_card_selector("u").values())[0])
                computer_deck.append(list(random_card_selector("c").values())[0])
                continue_game = check_game_over(user_deck, computer_deck, "n")
            elif continue_game=='n':
                continue_game = check_game_over(user_deck, computer_deck, "y")
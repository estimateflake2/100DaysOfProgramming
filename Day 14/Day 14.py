#========================== Higher or Lower Game
# In this game, the player guesses which of two choices has a higher follower count.
# A correct guess earns 1 point and allows the game to continue.
# An incorrect guess ends the game and displays the final score based on total correct guesses.
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print (logo)
import game_data
from random import randint

used_data_tracker = []
#{'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'}
def print_n_collectinput(new_compare):
    print(f"\n\n\nCompare A: ", new_compare[0]['name'], ", ", new_compare[0]['description'], ", from ", new_compare[0]['country'], ".",
          vs,
          "B: ", new_compare[1]['name'], ", ", new_compare[1]['description'], ", from ", new_compare[1]['country'], ". \n")
    usr_input = str(input("Who has more followers? Type 'A' or 'B': "))
    return usr_input

def get_new_compare ():
    if len(used_data_tracker) == len(game_data.data):
        return False
    ran_gen = randint(0, len(game_data.data) - 1)
    while ran_gen in used_data_tracker and len(used_data_tracker) < len(game_data.data):
        ran_gen = randint(0, len(game_data.data) - 1)
    used_data_tracker.append(ran_gen)
    return game_data.data[ran_gen]

def add_new_compare(usr_inp, old_compare):
    return_compare = []
    new_compre = get_new_compare ()
    if usr_inp == 'A':
        return_compare[0] = old_compare[0]
    elif usr_inp == 'B':
        return_compare[0] = old_compare[1]
    if new_compre != False:
            return_compare [1] = new_compre
    else:
        return False
    return return_compare
def comp_results (usr_input, old_compare):
    if usr_input =='A':
        if (old_compare[0]['follower_count'] < old_compare[1]['follower_count']):
            return False
        else:
            return True
    elif usr_input =='B':
        if (old_compare[1]['follower_count'] < old_compare[0]['follower_count']):
            return False
        else:
            return True
compare = []
end_game = False
score = 0
compare.append(get_new_compare ())
compare.append(get_new_compare ())
cmp = get_new_compare ()
while not end_game:
    user_input = print_n_collectinput(compare)
    if comp_results (user_input, compare):
        score += 1
        print(f"You're correct! Current score: {score}")
    else:
        print (f"Sorry, that's wrong. Final score: {score}")
        end_game = True


















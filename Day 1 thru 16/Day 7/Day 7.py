#================== Hangman Project
#========================================== Variable Initialization
hangman_art = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
    """
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
curr_stage = len(stages) - 1
str = ["school", "best friend", "mom","car", "run"]
lives = 6
dash = ""
def replaceString (g_dash, g_indexes, g_usr_inp):
    ret_str = []
    for n in g_dash:
        ret_str.append(n)

    for g_i in g_indexes:
        ret_str[g_i] = g_usr_inp
    return "".join(ret_str)


#=================================================================================

print(hangman_art)
for index, word in enumerate(str):
    dash = ""
    lives =6
    for letter in word:
        if letter.isalpha(): dash +="_"
        else: dash +=" "
    i =0
    while  lives > 0 and dash.__contains__("_"):
        i += 1
        print(f"*****************************{lives}/6 LIVES LEFT *****************************")
        print (f"Word to guess: {dash}")
        usr_input = input(f"Guess a letter: ").strip()
        if usr_input[0] in word:
            indexes = []
            for ii in range(len(word)):
                if word[ii] in usr_input[0]:
                   indexes.append(ii)
            dash = replaceString (dash, indexes, usr_input[0])
            if (not dash.__contains__("_")):
                print(f"Great Job! You Won! {dash}")
            else:
                print(f"You rock! Keep it going ")
        else:
            lives -= 1
            if lives == 0:
                print(f"Sorry, you lose! The word was {word}")
            else:
                curr_stage -=1
                print (f"You guessed {usr_input}, that's not in the word. You lose a life.\n {stages[curr_stage]} ")



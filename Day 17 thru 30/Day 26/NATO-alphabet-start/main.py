import pandas as pand

df = pand.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

while True:
    word = input (" Enter a word: ")
    translate = [phonetic_dict[letter.upper()] for letter in word]
    print (translate)

    import random
    
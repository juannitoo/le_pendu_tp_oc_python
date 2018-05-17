# -*-coding:Utf-8 -*
import fonctions
from donnees import tries_number
import os

print("""Bienvenue, on va jouer au jeu du pendu. 
        Vous sélectionnez une lettre et cherchez le mot""")

# I initialize game vars
# the word to discover
mystery_word = fonctions.mystery_word()
# a tuple containing :
starred = fonctions.starred_word(mystery_word)
# the hidden word with stars
starred_word = starred[0]
# and the word's character list eg: ['a', 'b', ...]
list_word = starred[1]

# i ask the playername
playername = input('rentrez votre nom : ')
# i print the player score if one is present
fonctions.print_player_score(playername)
print('Devinez le mot : ',starred_word)


i = 0
# 10 chances
while i < tries_number:
    # i ask player to choose a character
    user_char = input('Choisissez votre caractère : ').lower()
    # i send the char and the hidden word ( ****a** ou a***a** )
    test_user_char = fonctions.test_char(user_char, list_word, starred_word)
    # i print the new modified hidden word
    starred_word = test_user_char
    print(starred_word)
    # i ask player to choose a word
    user_answer = input("Essayer de déviner le mot ou appuyer sur start (reste " + str(10-i) + " chances) : ").lower()  
    # i test the word and print in consequencies
    test_user_answer = fonctions.test_answer(user_answer, mystery_word, playername)
    if test_user_answer == True:
        break
    else:
        print(starred_word)
    if i == 9:
        print("""Vous avez perdu ! Ooh le mauvais ! 
        tu peux tricher en regardant le fichier donnees.py !
        solution : """, mystery_word)
        fonctions.print_score()
    i += 1


# pour windows
os.system("pause")
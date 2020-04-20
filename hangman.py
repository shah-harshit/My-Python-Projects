import numpy as np
import random

GAME_OVER = False
ATTEMPTS = 5


def if_lost(ATTEMPTS,GAME_OVER):

    if ATTEMPTS == 0:
        print("\nYOU LOST, BETTER LUCK NEXT TIME!!!")
        GAME_OVER = True

    return GAME_OVER


def user_input(choice):
    change = 0
    for a in range(word_len):
        if choice.casefold() != word[a]:
            pass
        else:
            hidden_word[a] = choice.casefold()
            change += 1

    print(' '.join(hidden_word))
    return change


def if_won(hidden_word,GAME_OVER):
    inc = 0
    for r in range(word_len):
        if hidden_word[r] != '_':
            inc += 1

    if inc == word_len:
        print("\nCONGRATULATIONS, YOU WON!!")
        GAME_OVER = True
        return GAME_OVER


ans = input("\nType 'y' to start the game : ").casefold()

while ans == 'y':

    random_word = np.array(['hella', 'india', 'pakistan', 'australia', 'japan'])
    word = str(random_word[random.randint(0, 4)])
    word_len = len(word)
    hidden_word = list("_" * word_len)
    used = str(' ')

    print("\nWELCOME TO HANGMAN!!")
    print(' '.join(hidden_word))

    while not GAME_OVER:
        choice = str(input("\nEnter an alphabet: "))

        if user_input(choice) == 0:
            ATTEMPTS -= 1

        used = used + ' ' + choice
        print('words used:' + used)

        if if_lost(ATTEMPTS,GAME_OVER):
            break

        elif if_won(hidden_word,GAME_OVER):
            break

        print("Attempts left: " + str(ATTEMPTS))

    ans = input("Type 'y' to start another game : ").casefold()

print("THANK YOU FOR PLAYING, COME BACK AGAIN")
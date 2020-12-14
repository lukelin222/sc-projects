"""
File: hangman.py
-------------------------------
This file demonstrates a Python Console hangman game.
At the beginning of the game, users are asked to input
one letter at a time to guess out a dashed vocabulary (answer).
If the letter is in the answer, the Console updates the
dashed word to its current status. 7 wrong guesses end the game.
"""

import random

# Constant
N_TURNS = 7


def main():
    """
    TODO:
    """
    #declare constants and variables
    answer = random_word()
    inputs = ""
    turns = N_TURNS

    #start main loop
    while True:
        #generate dashed text and check if all characters are guessed
        dashed = ""
        incorrect = 0
        for char in answer:
            if char in inputs:
                dashed += char
            else:
                dashed += "-"
                incorrect += 1
        #check if game ended
        if incorrect == 0:
            print("you win!!")
            break
        elif turns == 0:
            print("You are completely hung : (")
            break

        #print dashed text ,show turns left
        print("The word looks like: {}".format(dashed))
        print("You have {} guesses left.".format(turns))

        #ask for input and check for illegal input
        while True:
            input_ch = input("Your guess: ").upper()
            if len(input_ch) > 1 or not str.isalpha(input_ch):
                print("illegal format.")
            else:
                break

        #check guess and print feedback
        inputs += input_ch
        if input_ch not in answer:
            print("There is no {}'s in the word.".format(input_ch))
            turns -= 1
        else:
            print("You are correct!")

    #show correct answer when game ends
    print("The word was: {}".format(answer))

def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

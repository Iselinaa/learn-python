import os
import random

alphabeta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersFound = []
tries = 5
words = ['HOUSE', 'ENTER THE CAR', 'UNDER THE TABLE', 'MY LITTLE PONY', 'TV']
word = words[random.randint(0, len(words) - 1)]

def displayWord(string, showLetters):
    hiddenWord = string
    for letter in alphabeta:
        if letter not in showLetters:
            hiddenWord = hiddenWord.replace(letter, '_')
    print(hiddenWord)

while tries > 0:
    displayWord(word, lettersFound)
    print("")
    gameFinished = True
    for letterIndex in range(0, len(word)):
        letter = word[letterIndex]
        if letter != " "  and letter not in lettersFound:
            gameFinished = False
            break
    if gameFinished:
        print("Congrats! You WON!")
        break

    guessLetter = input("Say a letter: ").upper()
    if guessLetter == 'SOLVE':
        guessWord = input("Say the word: ").upper()
        if guessWord == word:
            for letterIndex in range(0, len(word)):
                letter = word[letterIndex]
                if letter != " "  and letter not in lettersFound:
                    lettersFound.append(letter)
            continue
        else:
            print("Wrong guess!")
            tries -= 1
            if tries == 1:
                print("You have " + str(tries) + " try left! Last chance!")
            elif tries > 0:
                print("You have " + str(tries) + " tries left! Try again!")
            continue 
    if guessLetter not in alphabeta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Wrong input!")
        continue
    os.system('cls' if os.name == 'nt' else 'clear')

    if guessLetter in word:
        lettersFound.append(guessLetter)
    else:
        print("This letter does not exist!")
        tries -= 1
        if tries == 1:
            print("You have " + str(tries) + " try left! Last chance!")
        elif tries > 0:
            print("You have " + str(tries) + " tries left! Try again!")
    
if tries == 0:
    print('You lost!' )
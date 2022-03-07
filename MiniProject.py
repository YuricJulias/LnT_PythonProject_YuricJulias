from os import sep
import random
from word import wordList

print("Welcome to Word Guesser Game")
play = input("Do you want to play (yes/no)? ").lower()

while play == "yes":

    randomWord = random.choice(wordList)
    print(randomWord)
    userGuess = input("\nGuess an character: ").lower()[0]
    chance = 10

    while chance > 0:
        wrongGuess = 0
        for character in randomWord:
            if character in userGuess:
                print(character, end="")
            else:
                wrongGuess += 1
                print("_", end="")

        if wrongGuess == 0:
            print(f"\n\nWell Played, the word is {randomWord}.\n")
            break

        guess = input("\n\nGuess another character: ").lower()[0]
        userGuess += guess

        if guess not in randomWord:
            chance -= 1
            print(f"Chance: {chance} left")

            if chance == 0:
                print(f"\nNice try the word is {randomWord}.")
    
    again = input("Do you want to play again (yes/no)? ").lower()
    if again != "yes":
        print("Good Game, ", end="")
        play = "no"

print("Bye :D")


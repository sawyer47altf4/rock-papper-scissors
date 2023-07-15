import time
import random
print("welcome")
imposorpos = input("do you want to play hard or normel rock papper scissors. answer with hard or normel: ")
# ^ picks the game mode between hard and normel
score = 0
if imposorpos == "hard":
# ^ checks for the game mode.
#the hard game mode is impossible to win
    while True:
        choese = input("choese r, p, s :")
        # ^ finds out what you pick and plays the winning answer
        time.sleep(0.5)
        if choese == "r":
            print("i pick p i win")
        elif choese == "p":
            print("i pick s i win")
        elif choese == "s":
            print("i pick r i win")
        score = score + 1
        print(score)
elif imposorpos == "normel":
    while True:
        ai = random.choice(["rock", "papper", "scissors"])
    # the ai/random mod pick out what to play
        choese = input("choese r, p, s :")
        print("i pick " + ai)
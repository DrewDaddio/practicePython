#ex.8: Rocks Paper Scissors
# Make a two-player Rock-Paper-Scissors game.
import sys
import random

player = input("What's your name?")
print(player + " do you want to play Rocks Paper Scissors?")


game = {'rock': 1, 'paper': 2, 'scissors': 3}
choice = str.lower(input("Pick rock, paper, or scissors "))


for x in range(1):
    comp = random.randint(1,4)


#ex.8: Rocks Paper Scissors
# Make a two-player Rock-Paper-Scissors game.
import sys
import random

name = input("What's your name?")

play = str.lower(input((name + " do you want to play Rocks Paper Scissors? ")))
def choice(option):
    if play == "yes":
        print("Let's play")
    else:
        sys.exit()

game = ['rock', 'paper', 'scissors']
bot = random.choice(game)
ask = input("Pick rock, paper, or scissors ")

def puzz():
    if ask == 'rock' and bot == 'rock':
        print("The computer chose " + bot + " so " + "tie play again")
    elif ask == 'rock' and bot == 'paper':
        print("The computer chose " + bot + " so " + "you lose")
    elif ask == 'rock' and bot == 'scissors':
        print("The computer chose " + bot + " so " + "you win")
    elif ask == 'paper' and bot == 'paper':
        print("The computer chose " + bot + " so " + "tie play again")
    elif ask == 'paper' and bot == 'scissors':
        print("The computer chose " + bot + " so " + "you win")
    elif ask == 'paper' and bot == 'rock':
        print("The computer chose " + bot + " so " + 'you lose')
    elif ask == 'scissors' and bot == 'paper':
        print("The computer chose " + bot + " so " + "you win")
    elif ask == 'scissors' and bot == 'scissors':
        print("The computer chose " + bot + " so " + "tie play again")
    elif ask == 'scissors' and bot == 'rock':
        print("The computer chose " + bot + " so " + 'you lose')
    else:
        print('please choose:\nrock\npaper\nscissors')

print(puzz())

if str.lower(input("Do you want to play again?")) == "yes":
    askAgain = ask
    askAgain
    botAgain = bot
    botAgain
    print(puzz())
else:
    sys.exit()
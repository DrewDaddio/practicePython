### Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
###

name = input("Hey You! What is your name? ")
print("Nice to meet you, " + name + "!")
print("Ready to do the 2nd exercise?")

number = int(input("Guess a number " + name + "."))

if number % 4 == 0:
    print(str(number) + " is a multiple of 4")
elif number % 2 == 0:
    print(str(number) + " is an even number")
else:
    print(str(number) + " is an odd number")

print("Great, now let's get 2 numbers")

check = int(input("Give me another number"))

if number % check == 0:
    print("Both numbers you gave divide evenly")
else:
    print("The numbers don't divide evenly.\n\n\n Womp Womp")
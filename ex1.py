# Exercise 1: Character Input

print("The challenge is to create a program that asks the user to enter their name and their age.")
print("Print out a message addressed to them that tells them the year that they will turn 100 years old.")

print("Hey you!")
name = input("What is your name?: ")
print("Your name is " + name)

print("Hey " + name)
age = input("What is your age?: ")
print("Your age is: " + age)

ageInt = int(age)
print("In 100 years you'll be " + str(int(100 + ageInt)) + " years old!")

year = str((2018 - ageInt) + 100)
print(name + " , you will turn 100 in the year " + year)
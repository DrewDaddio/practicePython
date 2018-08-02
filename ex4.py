#ex4: Create a program that asks the user for a number
# and then prints out a list of all the divisors of that number.

print("Ready for exercise 4?")
number = int(input("Give me a number!: "))


x = list(range(2,number + 1))
divisor = []

for i in x:
    if number % i == 0:
        divisor.append(i)

print(divisor)
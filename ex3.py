# ex.3 List less than 10
#Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

print('Let\'s take a look at the list')

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)

print("now let's see only the numbers less than 5")

b = []

for i in a:
    if i < 5:
        b.append(i)

print(b)
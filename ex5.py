# ex5.Take two lists
# write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Try to randomly generate lists

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

print(a)
print(b)
print("that's list a & b. Now let's see the elements that match")
for i in a:
    if i in b:
        c.append(i)

print("Here's what matches")
print(c)

d = random.sample(range(1,20),10)
e = random.sample(range(1,30),15)

print(d)
print(e)
f = []

for k in d:
    if k in e:
        f.append(k)

print("Let's see what matches this now")
print(f)
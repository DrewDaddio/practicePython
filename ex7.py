#ex.7
#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("check out this list.")
print(a)

print("Let's just show the even numbers.")

b = [element for element in a if element % 2 == 0]
print(b)
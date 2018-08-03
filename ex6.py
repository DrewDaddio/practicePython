#ex6.Ask the user for a string
# and print out whether this string is a palindrome or not

words = str.lower(input("Tell me a word: " ))

print("The word you chose is " + words + ".")

rev = words[::-1]

if rev == words:
    print("That's a palindrome")
else:
    print("That's not a palindrome")

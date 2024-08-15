# Write a python program to sort words in alphabetical order.
alphabet = str(input("enter a statement : "))
words = [x.lower() for x in alphabet.split()]

words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)

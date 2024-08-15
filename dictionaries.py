## Dictionary
# Dictionaries are a kind of data type in python, and they are always represented using curly brackets
# Dictionaries are represented in the form of key-value pair
# All the keys in a dictionary are unique, though dictionary can have same values
# Key value pair together form an item
# Dictionary values can only be accessed through the keys

sample = {"item1" : "value1", 164 : "test", 203 : "value2", 184 : "value2", 164 : "updated value"}
print(sample)

print("\n")

## Check all keys in dictionary
print(sample.keys())

print("\n")

##Check all values in dictionary
print(sample.values())

print("\n")
## Check items in dictionary
print(sample.items())

print("\n")
## Accessing items in a dictionary

# Items can only be accessed through the keys
print(sample["item1"])
print("\n")

## Adding items to dictionary in the form of key-value pair
sample["name"] = "Bryan"
print(sample)
print("\n")

## Deleting an item from dictionary can be done using the command del
del(sample[164])
print(sample)
print("\n")

## Modifying value in a dictionary
sample["name"] =  "Ryan"
print(sample)
print("\n")

sample["name"] =  "mike"
print(sample)
print("\n")

sample["food"] =  "fish and chips"
print(sample)
print("\n")

del(sample["food"])
print(sample)
print("\n")

print(sample["name"])
print("\n")

sample["drink"] =  "coke"
print(sample)
print("\n")

sample["animal"] = "Tiger"
print(sample)
print("\n")

sample["animal2"] =  "Gorilla"
print(sample)
print("\n")

if "animal2" in sample:
  print("The key exsits in dictionary")

else:
  print("The key is not in dictionary")


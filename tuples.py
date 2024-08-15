## Tuples are another kind of data in python. They are always represented using round brackets
# Tuples contain different types of data like integer, float, string list and tuple itself
# Tuples also follow similar concepts of indexing and slicing like lists
# Tuples are immutable, which means we cannot modify them once they are defined
# Tuples have the concept of unpacking, using which we can assign unique variable name to each value


bc = (846, 13.74, "123 abc###", True, ["Travel like me!", 23, False, 24.94 ])
print(bc, type(bc))

test1 = "Bryan", 13, "abc street", "ZHC372"
print(test1, type(test1))

test2 = 18.0000, 18
print(test2, type(test2))

# Unpacking - Through unpacking concept, we can decongest a variable value into separate variables
Name, Age, Location, Zipcode = test1

print("My name is : ", Name)
print("My age is : ", Age)
print("My address is : ", Location)
print("My postcode is : ", Zipcode)

abc = (846, 13.74, "123 abc###", True, ["Travel like me!", 23, False, 24.94 ])

print(abc[3])
print(abc[-4])
print(abc[2][4])
print(abc[-3][-4])
print(abc[4][0][7])



print(abc[2:4])
print(abc[1:7])
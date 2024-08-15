### Lists ###
# Lists are one of the data type in python. They are represented using square brackets
# Lists can contain different types of data like integer, floats, strings, tuples, including lists as well
# Lists within a list are known as nested lists
# Lists have the property of indexing. Every item in a list has an index value. Index value are of two 
# types : Positive and Negative Positive index arein the direction from left to right, starting from 0,1,2...
# Negative index is in reverse direction i.e from right to left and it starts with -1, -2, ...
# Lists also have the property of slicing, where we can extract a portion from within the list by passing 
# index values

abc = [846, 13.74, "123 abc###", True, ["Travel like me!", 23, False, 24.94 ]]
print(abc, type(abc))

# Indexes are nothing but positional values
print(abc[3])
print(abc[-4])
print(abc[2][4])
print(abc[-3][-4])
print(abc[4][0][7])

## Slicing - It is used to extract list or a portion within a list
# abc[1:3], 1 is starting index 3 is ending index, so it always starts from starting index and goes upto 1 
# less than the ending index


print(abc[2:4])
print(abc[1:7])
print(abc[:])

# Slicing needs to be done again next class, as concept is not clear for Bryan

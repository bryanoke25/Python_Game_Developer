### SETS ###
# Sets are a collection of well defined items and are represented using curly brackets {}
# Sets do not store  duplicate values . If duplicate values are mistakenly  enetered, it discards them
# Sets do not have the concept of indexing in them
# Sets always stores items of similar datatype
# Sets have four major operations : Union, Intersection, Difference and Symmetric Difference

sample_set = {1, 2, 3, 4, 11, 22, 33, 44, 22}
print(sample_set)

# Check if an item exists in a set or not
if 33 in sample_set:
    print("Yes, the item exists")
else:
    print("No, the item does not exist")

## Adding an item to a set
sample_set.add(13)
sample_set.add(24)
print(sample_set)

## Removing an item from a set
sample_set.remove(2)
print(sample_set)


set1 = {1, 2, 3, 4, 6}
set2 = {4, 6, 7, 8, 9}

# Union - It combineas item of both the sets and discards duplicate items
print(set1.union(set2))

# Intersection - Items which are common in both the sets
print(set1.intersection(set2))

# Difference -> A-B means displaying items of A by removing common items of B
print(set1.difference(set2))
print(set2.difference(set1))

# Symmetric difference - It is just like union of two sets, but the common items are rejected here
print(set1.symmetric_difference(set2))
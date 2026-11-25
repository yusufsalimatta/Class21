my_set = {1, 2, 3}
print(my_set)


# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set Cannot Have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# We Can Make Set From A List
my_set = set([1, 2, 3, 2])
print(my_set,"\n")


# Remove A Number
numset = set([0, 1, 3, 4, 5])
print("Orignal Set:")
print(numset)
numset.pop()

print("After Removing The First Element From The Said Set:")
print(numset,"\n")


# read the two lists of pairs of integers
list1 = eval(input())
list2 = eval(input())

# convert each pair into a set to make order irrelevant
set1 = set(map(frozenset, list1))
set2 = set(map(frozenset, list2))

# calculate the intersection of the two sets
common = set1 & set2

# print the number of common pairs
print(len(common))
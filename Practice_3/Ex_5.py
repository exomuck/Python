from itertools import zip_longest

def remove_duplicates(l):
  # YOUR CODE HERE
  res = [i for i, j in zip_longest(l, l[1:]) if i != j]
  return res
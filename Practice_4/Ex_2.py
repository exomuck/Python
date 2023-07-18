import numpy as np
def convert(arr):
    row_sums = arr.sum(axis=1)
    return arr / row_sums[:, np.newaxis]

print(convert(np.arange(0, 9).reshape(3, 3)))
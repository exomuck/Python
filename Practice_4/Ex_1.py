import numpy as np

rows, cols = np.indices((4, 5))
arr = np.where(rows < 3, (rows + 1) + 5 * cols, (rows - 2) + 5 * cols)

print(arr)
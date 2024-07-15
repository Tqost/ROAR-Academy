import numpy as np


def swap_rows(M, a, b):
    if type(M) != np.ndarray:
        raise TypeError("Cannot swap something that isn't array")
    if type(a) != int or type(b) != int:
        raise TypeError("Cannot swap without an integer")
    row, col = M.shape
    if row < 2 or col < 2:
        raise TypeError("Array must be larger than 2")
    if a > row or b > row:
        raise TypeError("Index of swapping rows must be in array")
    row_a = np.array(M[a - 1])
    M[a - 1] = M[b - 1]
    M[b - 1] = row_a
    return M


def swap_cols(M, a, b):
    if type(M) != np.ndarray:
        raise TypeError("Cannot swap something that isn't array")
    if type(a) != int or type(b) != int:
        raise TypeError("Cannot swap without an integer")
    row, col = M.shape
    if row < 2 or col < 2:
        raise TypeError("Array must be larger than 2")
    if a > col or b > col:
        raise TypeError("Index of swapping columns must be in array")
    col_a = np.array(M[0:, a - 1])
    M[0:, a - 1] = M[0:, b - 1]
    M[0:, b - 1] = col_a
    return M


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(swap_rows(arr, 1, 3))
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(swap_cols(arr, 1, 3))

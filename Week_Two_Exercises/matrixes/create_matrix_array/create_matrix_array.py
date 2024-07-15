import numpy as np


def set_array(L, rows, cols, order):
    if type(L) != list:
        raise TypeError("Must be list variable")
    if type(rows) != int or type(cols) != int:
        raise TypeError("Rows and cols must be integers")
    if order not in ["F", "C"]:
        raise TypeError('Order must be "F" or "C"')
    array = np.array(L)
    array = np.reshape(array, (3, 3), order)
    return array


list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(set_array(list_, 3, 3, "F"))
print(set_array(list_, 3, 3, "C"))

''' https://stackoverflow.com/questions/17370820/python-slice-notation-with-comma-list

This is known as advanced indexing, and picks out the specified columns:

Numpy arrays and pandas dataframes use 2-d arrays.

The first argument typically represents a slice of rows, while the second represents a slice of columns.

So array[:, :3] would be all rows, first three columns.

'''


import numpy as np
a = np.arange(12).reshape(3, 4)
print(a)
''' [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

 '''

print(a[:, [1,2,3]])

''' [[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]]

'''
print(a[:, [1,3]])

'''
[[ 1  3]
 [ 5  7]
 [ 9 11]]

'''

'''
IMPORTANT - Note that this won't work with the standard Python list:
'''

a.tolist()
[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
a.tolist()[:,[1,2,3]]
# list indices must be integers or slices, not tuple
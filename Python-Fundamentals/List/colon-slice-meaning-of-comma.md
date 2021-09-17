
### Meaning of comma in slice notation like - `plt.scatter(X_p[:,0], X_p[:,1])`

```py

import numpy as np

x = np.random.rand(3, 2)
print(x)

"""
[[0.81733476 0.25943479]
 [0.22755117 0.14142344]
 [0.13767046 0.03423801]]
"""


y = x[:, 1]
print(y)

# [0.25943479 0.14142344 0.03423801]

```

#### So what that line did is sliced the array, taking all rows (:) but keeping the second column (1)

it is simply like you are specifying the axis. Consider the starting column as 0 then as you go through 1,2 and so on.

The syntax is `x[row_index,column_index]`

#### you can also specify a range of row values as per need in row_index also eg:1:13 extracts first 13 rows along with whatever specified in column

---

Assuming that the object is really a `numpy` array, this is known as [advanced indexing](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#advanced-indexing), and picks out the specified columns:

Note that this won't work with the standard Python list:

```py

import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)


""" array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])

"""


print(a[:, [1, 2, 3]])


"""

array([[ 1,  2,  3],
       [ 5,  6,  7],
       [ 9, 10, 11]])

"""

print(a[:, [1, 3]])


"""

array([[ 1,  3],
       [ 5,  7],
       [ 9, 11]])

"""

```

#### Note again that this won't work with the standard Python list:

```py

import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

a.tolist()
print(a.tolist()[:, [1, 2, 3]])

```

Will throw

```
TypeError: list indices must be integers, not tuple
```
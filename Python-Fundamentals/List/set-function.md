https://www.geeksforgeeks.org/python-set-method/

Set, a term in mathematics for a sequence consisting of distinct language

set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set.

Syntax : set(iterable)
Parameters : Any iterable sequence like list, tuple or dictionary.
Returns : An empty set if no element is passed. Non-repeating element iterable modified as passed as argument.

Sets are unordered.

Use `sorted(set(sampleList))` to get it sorted

---

### Convert sets to list

```python

my_set = set([1,2,3,4, 2])
print(my_set)
# {1, 2, 3, 4}

# thats why need to convert to list
my_list = list(my_set)
print(my_list)
# [1, 2, 3, 4]

```

### Modifying a set in Python

https://www.programiz.com/python-programming/set

#### Sets are mutable. However, since they are unordered, indexing has no meaning.

We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.

We can add a single element using the `add()` method, and multiple elements using the update() method. The `update()` method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

```python

# initialize my_set
my_set = {1, 3}
print(my_set)
# {1, 3}

my_set[0]
# if you uncomment above line ,
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
my_set.add(2)
print(my_set)
# Output: {1, 2, 3}

my_set.update([2, 3, 4])
print(my_set)
# Output: {1, 2, 3, 4}


# add list and set
my_set.update([4, 5], {1, 6, 8})
print(my_set)
# Output: {1, 2, 3, 4, 5, 6, 8}

```

---

### Removing elements from a set

A particular item can be removed from a set using the methods discard() and remove().

The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set. On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).

```python

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
my_set.discard(4)
print(my_set)
# Output: {1, 3, 5, 6}

# remove an element
my_set.remove(6)
print(my_set)
# Output: {1, 3, 5}

# discard an element
# not present in my_set
my_set.discard(2)
print(my_set)
# Output: {1, 3, 5}

# remove an element
# not present in my_set
# you will get an error.
my_set.remove(2)
# Output: KeyError

```

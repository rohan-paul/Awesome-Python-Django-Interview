#### In Python, there are two ways, sort() and sorted(), to sort lists (list) in ascending or descending order.

#### If you want to sort strings (str) or tuples (tuple), use sorted().

### sort() is a destructive process that sort the original list in place. And thats why sort() method can not used on strings and tuples as they are immutable. And sort() method will update the original object.

```python

org_list = [3, 1, 4, 5, 2]

org_list.sort()
print(org_list)
# [1, 2, 3, 4, 5]

```

By default, the list is sorted in ascending order. If you want to sort in descending order, set the parameter reverse to True.

```python

org_list.sort(reverse=True)
print(org_list)
# [5, 4, 3, 2, 1]

```

---

### Specifying a list to sorted() returns a sorted list. The original list remains unchanged.

```python

org_list = [3, 1, 4, 5, 2]

new_list = sorted(org_list)
print(org_list)
print(new_list)
# [3, 1, 4, 5, 2]
# [1, 2, 3, 4, 5]

```

Like sort(), by default, the list is sorted in ascending order. If you want to sort in descending order, set the parameter reverse to True.

```python
new_list_reverse = sorted(org_list, reverse=True)
print(org_list)
print(new_list_reverse)
# [3, 1, 4, 5, 2]
# [5, 4, 3, 2, 1]
```

---

#### How to sort strings and tuples

##### Since strings and tuples are immutable, there is no sort() method that update the original object.

##### On the other hand, you can specify not only lists but also strings and tuples to the sorted() function that creates a new sorted list. Since sorted() returns a list, it must be converted to a string or tuple.

```python

new_str_list = sorted(org_str)
print(org_str)
print(new_str_list)
# cebad
# ['a', 'b', 'c', 'd', 'e']

```

Use the join() method to concatenate a list of characters into a single string.

```python

new_str = ''.join(new_str_list)
print(new_str)
# abcde

```

You can write in one line. If you want to sort in descending order, set the argument reverse to True.

```python

new_str = ''.join(sorted(org_str))
print(new_str)
# abcde

new_str_reverse = ''.join(sorted(org_str, reverse=True))
print(new_str_reverse)
# edcba

```

---

### Sort tuples

Sorting tuples is the same as for strings. Passing a tuple to sorted() returns a sorted list.

```python

org_tuple = (3, 1, 4, 5, 2)

new_tuple_list = sorted(org_tuple)
print(org_tuple)
print(new_tuple_list)
# (3, 1, 4, 5, 2)
# [1, 2, 3, 4, 5]
```

To convert a list to a tuple, use tuple().

```python

new_tuple = tuple(new_tuple_list)
print(new_tuple)
# (1, 2, 3, 4, 5)

```

You can write in one line. If you want to sort in descending order, set the argument reverse to True.

```python

new_tuple = tuple(sorted(new_tuple_list))
print(new_tuple)
# (1, 2, 3, 4, 5)

new_tuple_reverse = tuple(sorted(new_tuple_list, reverse=True))
print(new_tuple_reverse)
# (5, 4, 3, 2, 1)

```

---

[Source](https://note.nkmk.me/en/python-list-sort-sorted/)

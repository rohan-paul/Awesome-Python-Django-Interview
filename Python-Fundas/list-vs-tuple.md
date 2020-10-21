#### The main difference between lists and tuples is the fact that lists are mutable whereas tuples are immutable.

A mutable data type means that a python object of this type can be modified.

An immutable object can’t.

Let’s create a list and assign it to a variable.

```
a = ["apples", "bananas", "oranges"]

# Let’s change “apples” to “berries”.
a[0] = "berries"

print(a)
# ['berries', 'bananas', 'oranges']
```

Now, what if we want to try the same thing with a tuple instead of a list? Let’s see.

```
>>> a = ("apples", "bananas", "oranges")
>>> a[0] = "berries"
Traceback (most recent call last):
  File "", line 1, in
TypeError: 'tuple' object does not support item assignment
```

https://www.afternerd.com/blog/difference-between-list-tuple/#:~:text=The%20Key%20Difference%20between%20a,mutable%20whereas%20tuples%20are%20immutable.&text=A%20mutable%20data%20type%20means,An%20immutable%20object%20can't.

---

#### Syntax Differences

Syntax of list and tuple is slightly different. Lists are surrounded by square brackets [] and Tuples are surrounded by parenthesis ().

```
list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)

# Output:

[1,2,3,4]
(1,2,3,4)
```

Find type of data structure using type() function

```
type(list_num)
type(tup_num)

# Output:

list
tuple
```

---

#### Python list method list()

Python list method list() takes sequence types and converts them to lists. This is used to convert a given tuple into list.

```
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)
print "List elements : ", aList

# List elements :  [123, 'xyz', 'zara', 'abc']

```

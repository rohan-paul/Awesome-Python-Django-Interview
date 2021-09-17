A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

The enumerate() function assigns an index to each item in an iterable object that can be used to reference the item later. What does enumerate do in Python? It makes it easier to keep track of the content of an iterable object.

If you are using enumerate in Python 3 and call `print(enumerate())`, you will get an alphanumeric memory reference address instead of a readable list. enumerate() in Python 3 works this way to save memory by not generating unnecessary full-fledged lists.

```py

cars = ['kia', 'audi', 'bmw']

for car in enumerate(cars):
  print(car)

# (0, 'kia')
# (1, 'audi')
# (2, 'bmw')


```

---

### Using enumerate() with range()

The last number of enumerate is not included i.e.



```py

cars = [(0, 2), (21, 13), (-23, -15), (22, 14), (23, 14)]

# In above I have 5 elements but to all of them I have to start
# at 1 and end at 6. Note 6-th is NOT included

for c, k in enumerate(range(1, 6)):
    # print(k[0])
    print(cars[c])


# (0, 2)
# (21, 13)
# (-23, -15)
# (22, 14)
# (23, 14)

```
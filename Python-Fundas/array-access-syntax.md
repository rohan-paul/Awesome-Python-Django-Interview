Assuming a is a string. The Slice notation in python has the syntax -

```
list[<start>:<stop>:<step>]

```

#### So, when you do `a[::-1]`, it starts from the end towards the first taking each element. So it reverses a. This is applicable for lists/tuples as well.

Example -

```python

a = '1234'

a[::-1]

# '4321'

```

Then you convert it to int and then back to string (Though not sure why you do that) , that just gives you back the string.

So, when I have a string `n = "abc"`

And I want to reverse it the solution

```
n[::-1]
```

It means, "start at the end; count down to the beginning, stepping backwards one step at a time."

Remember, [-1] means the last element in a sequence

```python

arr1 = [1, 2, 3, 4, 9, 12, 18]

# [-1] means the last element in a sequence, which in this is case is the list

print(arr1[::-1])
# [18, 12, 9, 4, 3, 2, 1]

print(arr1[-2:])
# [12, 18]

```

---

### Again lets see implementation of this syntax

```
list[<start>:<stop>:<step>]

```

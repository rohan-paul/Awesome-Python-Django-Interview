# What will be the output of the code below? Explain your answer.

def multipliers():
  return [lambda x : i * x for i in range(4)]

# print([m(2) for m in multipliers()])

''' Explanation

The output of the above code will be [6, 6, 6, 6] (not [0, 2, 4, 6]).

The reason for this is that Python’s closures are late binding.

See - https://en.wikipedia.org/wiki/Late_binding

This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by multipliers() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by 3, so since a value of 2 is passed in the above code, they all return a value of 6 (i.e., 3 x 2).

(Incidentally, as pointed out in The Hitchhiker’s Guide to Python, there is a somewhat widespread misconception that this has something to do with lambdas, which is not the case. Functions created with a lambda expression are in no way special and the same behavior is exhibited by functions created using an ordinary def.)
'''

# One solution would be use a Python generator as follows:
def multipliers_generator():
  for i in range(4): yield lambda x: i * x

print([m(2) for m in multipliers_generator()])

# Output - [0, 2, 4, 6]
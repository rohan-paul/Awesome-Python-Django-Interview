'''

__init__ does act like a constructor. You'll need to pass "self" to any class functions as the first argument if you want them to behave as non-static methods. "self" are instance variables for your class.

The self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python. It binds the attributes with the given arguments. The reason why we use self is that Python does not use the ‘@’ syntax to refer to instance attributes. In Python, we have methods that make the instance to be passed automatically, but not received automatically. '''

class food():


  def __init__(self, fruit, color):
    self.fruit = fruit
    self.color = color

  def show(self):
    print('fruit is ', self.fruit)
    print('color is ', self.color)


apple = food('apple', 'red')
grapes = food('grapes', 'green')

apple.show()
grapes.show()



'''

self is not implicitly available but is actually a required parameter to all methods of the class.


https://stackoverflow.com/a/2709832/1902852

Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on. That makes methods entirely the same as functions, and leaves the actual name to use up to you (although self is the convention, and people will generally frown at you when you use something else.) self is not special to the code, it's just another object.

'''
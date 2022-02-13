### What is self in Python?

https://www.programiz.com/article/python-self-why - GREAT


In object-oriented programming, whenever we define methods for a class, we use self as the first parameter in each case. Let's look at the definition of a class called Cat.

```py
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

```

In this case all the methods, including __init__, have the first parameter as self.

We know that class is a blueprint for the objects. This blueprint can be used to create multiple numbers of objects. Let's create two different objects from the above class.

```py
cat1 = Cat('Andy', 2)
cat2 = Cat('Phoebe', 3)

```

The self keyword is used to represent an instance (object) of the given class. In this case, the two Cat objects cat1 and cat2 have their own name and age attributes. If there was no self argument, the same class couldn't hold the information for both these objects.

However, since the class is just a blueprint, self allows access to the attributes and methods of each object in python. This allows each object to have its own attributes and methods. Thus, even long before creating these objects, we reference the objects as self while defining the class.


## Why is self explicitly defined everytime?

Let's take a simple example to begin with. We have a Point class which defines a method distance to calculate the distance from the origin.

```py
class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5

```
Let us now instantiate this class and find the distance.

```
>>> p1 = Point(6,8)
>>> p1.distance()
10.0

```

In the above example, __init__() defines three parameters but we just passed two (6 and 8). Similarly distance() requires one but zero arguments were passed. Why is Python not complaining about this argument number mismatch?

### What Happens Internally?

`Point.distance` and `p1.distance` in the above example are different and not exactly the same.


```py
>>> type(Point.distance)
<class 'function'>
>>> type(p1.distance)
<class 'method'>
```

We can see that the first one is a function and the second one is a method. A peculiar thing about methods (in Python) is that the object itself is passed as the first argument to the corresponding function.

In the case of the above example, the method call p1.distance() is actually equivalent to Point.distance(p1).

**Generally, when we call a method with some arguments, the corresponding class function is called by placing the method's object before the first argument. So, anything like obj.meth(args) becomes Class.meth(obj, args). The calling process is automatic while the receiving process is not (its explicit).**

**This is the reason the first parameter of a function in class must be the object itself.**
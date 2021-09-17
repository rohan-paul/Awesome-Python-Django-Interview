### whats-is-%s-and-%d-in-python-string-formatting

https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting/48660475

#### They are format specifiers. They are used when you want to include the value of your Python expressions into strings, with a specific format enforced.

More specifically, %s converts a specified value to a string using the str() function. Compare this with the %r conversion type that uses the repr() function for value conversion.

%s is used as a placeholder for string values you want to inject into a formatted string.

%d is used as a placeholder for numeric or decimal values.

For example (for python 3)

```python
print('%s is %d years old' % ('Joe', 42))

# Joe is 42 years old

```

#### Notice that the %s token is replaced by whatever I pass to the string after the % symbol. Notice also that I am using a tuple here as well (when you only have one string using a tuple is optional) to illustrate that multiple strings can be inserted and formatted in one statement.

---

They are used for formatting strings. `%s` acts a placeholder for a string while `%d` acts as a placeholder for a number. Their associated values are passed in via a tuple using the `%` operator.

    name = 'marcog'
    number = 42
    print '%s %d' % (name, number)
    # marcog 42

will print `marcog 42`. Note that name is a string (%s) and number is an integer (%d for decimal).

See https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting for details.

In Python 3 the example would be:

    print('%s %d' % (name, number))

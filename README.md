# Combine two lists as a dictionary | dict(zip)

Program

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)
```

Output

```bash
{'a': 1, 'b': 2, 'c': 3}
```

Program

```python
keys = ('name', 'age', 'location')
values = ('Soumik', 26, 'Bangladesh')

new_dict = dict(zip(keys, values))
print(new_dict)
```

Output

```bash
# output
{'name' : 'Soumik', 'age' : 26, 'location' : 'Bangladesh'}
```

# Create nested directory using pathlib

Program

```python
from pathlib import Path

Path("father/child").mkdir(parents=True, exist_ok=True)
```

# Slice Strings

Program

```python
# print the last character of the string
text = "abcd"
text[-1]
```

Output

```bash
'd'
```

Program

```python
# print everything but the last character
text = "abcd"
text[:-1]  # text[0: -1]
```

Output

```bash
'abc'
```

# Reverse a string using recursion

```python
def reverse_text(text):
    # base condition
    if text == "":
        return text
    else:
        return text[-1] + reverse_text(text[0:-1])
```

# append and extend in Python List

Program

```python
x = [1, 2, 3]
x.append([4, 5])
print (x)
```

Output

```bash
[1, 2, 3, [4, 5]]
```

Program

```python
x = [1, 2, 3]
x.extend([4, 5])
print (x)
```

Output

```bash
[1, 2, 3, 4, 5]
```

Program

```python
my_list = ['Python', 'Java']
my_list.append('Dart')
print(my_list)
```

Output

```bash
['Python', 'Java', 'Dart']
```

Program

```python
my_list = ['python', 'java']
another_list = [0, 1, 2, 3]
my_list.extend(another_list)
print(my_list)
```

Output

```
['python', 'java', 0, 1, 2, 3]
```

# Switch case in Python

Unlike every other programming language, Python does not have a switch or case statement.To get around this fact, we use dictionary mapping.

Program

```python
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "Data not available")


if __name__ == "__main__":

    result = numbers_to_strings(1)
    print(result)
```

Output

```bash
one
```

Program

```python
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "Data not available")


if __name__ == "__main__":

    result = numbers_to_strings(4)
    print(result)
```

Output

```bash
Data not available
```

# Read and Write File

Program

```python
# read mode only, if the file does not exists, raises I/O error

filename = open("new_file.txt", "a")
```

```python
# The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

filename = open("filename.txt", "a")
```

# List vs Tuple, when to use what

Tuples are fixed size in nature whereas lists are dynamic.
In other words, a tuple is immutable whereas a list is mutable.

1. You can't add elements to a tuple. Tuples have no append or extend method.
2. You can't remove elements from a tuple. Tuples have no remove or pop method.

Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences. Tuples have structure, lists have order.

Using this distinction makes code more explicit and understandable.

One example would be pairs of page and line number to reference locations in a book, e.g.:

```bash
my_location = (42, 11)  # page number, line number
```

You can then use this as a key in a dictionary to store notes on locations. A list on the other hand could be used to store multiple locations.

# yield keyword

`yield` is a keyword that is used like return, except the function will return a generator.

Generators do not store all the values in memory, they generate the values on the fly.

# Inheritance in Python

Program

```python
# define the base class

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name, self.last_name)


x = Person("Elon", "Musk")
x.print_name()
```

Output

```bash
Elon Musk
```

Program

```python
# create a subclass (Entrepreneur) that extends base class(Person)

class Entrepreneur(Person):
    pass
```

Program

```python
# Use the Entrepreneur class to create an object,
# and then execute the print_name method


sub_class_var = Entrepreneur("Elon", "Musk")
sub_class_var.print_name()
```

Output

```bash
Elon Musk
```

Program

```python
# When we add the __init__() function, the subclass will
# no longer inherit the parent's/base's __init__() function


class Entrepreneur(Person):
    def __init__(self, first_name, last_name):
    # add properties
```

```python
# we can add super() function that will make the child class
# inherit all the methods and properties from its parent +
# we can add it's own properties.


class Entrepreneur(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
```

Program

```python
class Entrepreneur(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        # adding new properties in the subclass
        self.company_name = "SpaceX"
```

# Polymorphism in Python

```python
# TODO
```

# Reverse a list

program

```python
language = ["Python", "Java", "Dart"]
language.reverse()
print(language)
```

Output

```bash
['Dart', 'Java', 'Python']
```

# Using generators inside functions

Program

```python
x = sum(i for i in range(10))
print(x)
```

Output

```bash
45
```

# Transpose a matrix

Program

```python
x = [[31, 17], [40, 51], [13, 12]]
print(list(zip(*x)))
```

Output

```bash
[(31, 40, 13), (17, 51, 12)]
```

================================================
AUTHOR: [SADMAN KABIR SOUMIK](https://www.linkedin.com/in/sksoumik/)

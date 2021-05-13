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

# Check the memory usage

Program

```python
import sys

a, b, c, d = "abcde", "xy", 2, 15.06
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
```

# Check if a file exists

Program

```python
import os.path

if os.path.isfile(filepath):
   print("File exists")
```

# Merge two dictionaries

Program

```python
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)
```

Output

```bash
{'a': 1, 'b': 3, 'c': 4}
```

# Make a flat list list out of lists of lists

Program

```python
import itertools

list_2d = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
merged = list(itertools.chain(*list_2d))
print(merged)
```

Output

```bash
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Program

```python
# using list comprehension

list_2d = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flat_list = [item for sublist in list_2d for item in sublist]
print(flat_list)
```

Output

```bash
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

# Slicing in array

Program

```python
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
```

# Find the index of an item in an array

Program

```python
list = ["Tensorflow", "PyTorch", "Caffe"]
idx_pytorch = list.index("PyTorch")
print(idx_pytorch)
```

Output

```bash
1
```

# Iterating over dictionaries using 'for' loops

Program

```python
d = {"x": 1, "y": 2, "z": 3}

for key, value in d.items():
    print(key, value)
```

Output

```bash
x 1
y 2
z 3
```

# Sort a dictionary by key

Program

```python
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sort_by_key = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
print(sort_by_key)
```

Output

```bash
{0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
```

# Sort dictionary by value

Program

```python
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sort_by_value = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
print(sort_by_value)
```

Output

```bash
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
```

# Rename all files of a folder

```python
import os

os.getcwd()
src_path = "./source_folder/"
destination_path = "./destination_folder/"

for i, filename in enumerate(os.listdir(src_path)):
    os.rename(src_path + filename, destination_path + str(i) + ".jpg")
```

# Count distinct elements in a list

Program

```python
from collections import Counter

words = ["a", "b", "c", "a", "b", "a"]

print(dict(Counter(words)))
# {'a': 3, 'b': 2, 'c': 1}
print(list(Counter(words).keys()))
# ['a', 'b', 'c']
print(list(Counter(words).values()))
# [3, 2, 1]
```

# Remove space and newlines from strings

Program

```python
s = "   \n\r\n  \n  abc   def \n\r\n  \n  "
remove_all = s.strip()
remove_left = s.lstrip()
remove_right = s.rstrip()

print(remove_all) # 'abc   def'
print(remove_left) # 'abc   def \n\r\n  \n  '
print(remove_right) # '   \n\r\n  \n  abc   def'
```

# Limit floats to two decimal places

Program

```python
a = 13.946
print("%.2f" % a)
```

Output

```bash
13.95
```

Program

```python
x = 13.946
print(round(x, 2))
```

Output

```bash
13.95
```

# Randomly select an item from an list.

```python
import random

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))
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

# Static methods in python

Program

```python
class MyClass:
    @staticmethod
    def the_static_method(x):
        print(x)


MyClass.the_static_method(2)  # outputs 2
```

Description

We can have static method in Python using `@staticmethod` decorator. Like other static methods in other languages, we don't need to create class instance to call the static method. We can directly call the static method using the Class name. Static methods are usually used to create utility functions.

================================================
AUTHOR: [SADMAN KABIR SOUMIK](https://www.linkedin.com/in/sksoumik/)

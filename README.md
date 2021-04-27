Maintained by SADMAN KABIR SOUMIK

---

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
keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')

new_dict = dict(zip(keys, values))
print(new_dict)
```

Output

```bash
# output
{'name' : 'Monty', 'age' : 42, 'food' : 'spam'}
```

# Create nested directory using pathlib

Program

```python
from pathlib import Path

Path("father/child").mkdir(parents=True, exist_ok=True)
```

# Slice texts using `:`

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

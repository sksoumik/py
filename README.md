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

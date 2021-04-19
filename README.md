Maintained by SADMAN KABIR SOUMIK

---

# Combine two lists as a dictionary | dict(zip)



```python
# program
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary) 
```

```bash
# output
{'a': 1, 'b': 2, 'c': 3}
```

```python
# program 
keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')

new_dict = dict(zip(keys, values))
print(new_dict)
```

```bash
# output
{'name' : 'Monty', 'age' : 42, 'food' : 'spam'}
```

# Create nested directory in the current directory | pathlib

```python
from pathlib import Path

Path("father/child").mkdir(parents=True, exist_ok=True)
```


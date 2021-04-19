# PYTHON BUILT-IN FUNCTIONS
Maintained by SADMAN KABIR SOUMIK

---

# dict(zip)

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


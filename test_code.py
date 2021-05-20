import collections

# remembers the order
d = collections.OrderedDict()
d["A"] = 65
d["C"] = 67
d["B"] = 66
d["D"] = 68

for key, value in d.items():
    print(key, value)

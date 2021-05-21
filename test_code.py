# def lcp(l):
#     s = ""

#     for c, *rest in map(set, zip(*l)):
#         if rest:
#             return s
#         s += c


# l = ["flower", "flow", "flight"]

# b = zip(*l)

# for i in b:
#     print(i)


def sum_lists(*args):
    return list(map(sum, zip(*args)))


a = [1, 2, 3]
b = [1, 2, 3]
c = [2, 3, 4]

result = sum_lists(a, b, c)
print(result)

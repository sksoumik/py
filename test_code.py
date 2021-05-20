from collections import Counter


def most_frequent(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]  # [0][0] is the first element of a matrix


list = [2, 1, 2, 2, 1, 3, 3, 3, 2]
print(most_frequent(list))
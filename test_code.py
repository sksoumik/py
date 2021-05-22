from collections import Counter


def find_duplicate(values):
    duplicates = Counter(values) - Counter(set(values))
    return list(duplicates.keys())


if __name__ == "__main__":
    values = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7]
    print(find_duplicate(values))

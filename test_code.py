# transpose a 2D matrix
def transpose(matrix):
    return list(zip(*matrix))


if __name__ == "__main__":
    print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

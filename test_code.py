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

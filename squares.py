
def get_squares():
    numbers = range(1, 21)
    return list(map(lambda x: x * x, numbers))


if __name__ == "__main__":
    print(get_squares())

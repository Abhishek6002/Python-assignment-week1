
def remove_duplicates(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


if __name__ == "__main__":
    numbers = [12,24,35,24,88,120,155,88,120,155]
    print(remove_duplicates(numbers))

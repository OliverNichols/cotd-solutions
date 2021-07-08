
def even_digits(a, b):
    result = []

    for num in range(a, b+1):
        for digit in map(int, str(num)):
            if digit % 2 != 0:
                break
        else:
            result.append(str(num))

    return ",".join(result)

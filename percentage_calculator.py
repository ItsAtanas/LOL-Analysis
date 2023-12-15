def calculate_percentage_equal(array1, array2):
    normal_length = len(array1)
    equal_count = 0
    for x, y in zip(array1, array2):
        if x == y:
            equal_count += 1

    percentage_equal = (equal_count / normal_length) * 100
    return percentage_equal

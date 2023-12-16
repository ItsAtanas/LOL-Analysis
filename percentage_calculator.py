def calculate_percentage_equal(winner, array2, normalized=False):
    total = len(winner)
    normal_length = len(winner)
    equal_count = 0
    for x, y in zip(winner, array2):
        if x == y:
            equal_count += 1
        elif y == '0':
             normal_length -= 1

    if normalized:
        percentage_equal = (equal_count / normal_length) * 100
    else:
        percentage_equal = (equal_count / total) * 100
    
    return percentage_equal

def calculate_percentage_equal_n2(winner, array2, array3):
    total = len(winner)
    normalized_total = len(winner)
    equal_count = 0
    print("before: ", normalized_total)
    for x, y, z in zip(winner, array2, array3):
        if x == y == z:
            equal_count += 1
        elif y == '0' or z == '0':
            normalized_total -= 1
    print("after: ", total - normalized_total)
    percentage_equal = (equal_count / normalized_total) * 100
    return percentage_equal

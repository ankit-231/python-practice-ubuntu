a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def times_2(n):
    return n * 2


mapped_array1 = map(times_2, a)
mapped_array2 = map(lambda x: x * 2, a)

print(list(mapped_array1))
print(list(mapped_array2))

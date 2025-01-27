# Sorting by keys

di = {"b": 15, "a": 20, "c": 17}
sorted_by_key = sorted(di.items())
print(sorted_by_key)  # [('a', 20), ('b', 15), ('c', 17)]

# Sorting by values
temp_li = []
for key, value in di.items():
    temp_li.append((value, key))

sorted_by_value = sorted(temp_li)
print(sorted_by_value)  # [(15, 'b'), (17, 'c'), (20, 'a')]

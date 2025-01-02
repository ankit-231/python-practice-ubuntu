def get_unique_element(li: list):
    temp_di = {}
    for index, item in enumerate(li):
        if item not in temp_di:
            temp_di[item] = 0
        else:
            temp_di[item] += 1
    print(temp_di)
    for k, v in temp_di.items():
        if v == 0:
            return k


li = [4, 3, 2, 1, 2, 3, 4]

print(get_unique_element(li))

def obtain_permutations(data, sum_data):
    data_copy = data.copy()
    data_permutations = data.copy()
    sum_value = 0
    i = 0
    count = 0
    while sum_value < sum_data:
        value = data_permutations[0]
        sum_value += value
        data_copy.remove(value)
        print(value, sum_value, sum_data, count, data_copy)
        count = obtain_permutations(data_permutations, sum_data-sum_value)
        if sum_value == sum_data:
            count += 1
    return count


data = [
    1,
    2,
    5,
    4,
    9,
    3,
    6,
    7
]
sum_data = 7
count = obtain_permutations(data, sum_data)
print(count)

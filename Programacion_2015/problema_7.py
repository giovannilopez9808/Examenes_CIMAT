def subset_sum(numbers, target, numbers_partial=[]):
    s = sum(numbers_partial)

    # check if the partial sum is equals to sum_data
    if s == sum_data:
        print("sum(%s)=%s" % (numbers_partial,
                              sum_data))
    if s >= sum_data:
        return   # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining,
                   sum_data,
                   numbers_partial + [n])


data = [1,
        2,
        5,
        4,
        9,
        3,
        6,
        7]
sum_data = 7
count = subset_sum(data, sum_data)
print(count)

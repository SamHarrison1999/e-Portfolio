def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


print(list_sum([1, 2, 3, 4, 5]))
print(list_sum([10, 12.5, 10, 7]))

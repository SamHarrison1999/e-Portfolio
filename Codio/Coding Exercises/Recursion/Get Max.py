def get_max(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0], get_max(nums[1:]))


print(get_max([1, 2, 3, 4, 5]))
print(get_max([11, 22, 3, 41, 15]))

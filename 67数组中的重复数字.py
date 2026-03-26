# 数组中重复数字

def func(nums: list):
    for i in nums:
        if nums.count(i) >= 2:
            return i
    return -1

print(func([1,2,3,3,5]))
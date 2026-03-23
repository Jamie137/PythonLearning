# 二分查找

# 给定一个元素升序的，无重复数字的整型数组nums和一个目标值target，存在则返回下标，否则返回-1

def func(nums, target):
    flag = len(nums) // 2
    while flag != 0:
        if nums[flag] < target:
            return func(nums[flag:], target)
        elif nums[flag] > target:
            return func(nums[:flag], target)
        else:
            return flag
    return -1


print(func([1,4,6,7,8,9,55] , 0))

# 实例

def func(nums, target):
    left = 0
    right = len(nums) - 1
    # 从数组的首尾开始，直到两个指针相遇
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1
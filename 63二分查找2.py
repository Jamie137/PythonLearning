# 二分查找2

# 有重复元素的升序数组，输出查找到的第一个对应元素的下标

def func(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = len(nums)//2
        if nums[middle] == target:
            temp = middle
            while nums[temp] == target and temp >= 0:
                temp -= 1
            return temp + 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle -1

    return -1

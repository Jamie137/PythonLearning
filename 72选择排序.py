# 选择排序

def selection_sort(nums: list):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
        # nums[i] = nums[i] if nums[i] < min(nums[i+1:]) else min(nums[i+1:])
        # if tmp != nums[i]
    return nums

print(selection_sort([20,1,6,4,89,3]))

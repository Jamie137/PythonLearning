# 冒泡排序

# 

nums = []

def bubble_sort(nums):
    for i in range(len(nums)):
        # 确保数组长度个元素都变成有序数列
        flag = False
        for o in range(len(nums) - i - 1):
            print(o)
            if nums[o] > nums[o + 1]:
                nums[o], nums[o + 1] = nums[o + 1], nums[o]
                flag = True

        if not flag:
            break
    return nums

print(bubble_sort([2,1,7,5,8,4,20,18,15]))
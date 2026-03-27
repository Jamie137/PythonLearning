# 插入排序

def insert_sort(nums: list):
    for i in range(1, len(nums)):
        j = i - 1 # 已排序列最右边的元素
        key = nums[i] # 待排序列最左边
        while j >= 0:
            if nums[j] > key:
                print(j)
                print(nums)
                print(nums[j + 1])
                nums[j+1] = nums[j]
                nums[j] = key
            j -= 1
    return nums

print(insert_sort([5, 78, 23, 1, 2]))
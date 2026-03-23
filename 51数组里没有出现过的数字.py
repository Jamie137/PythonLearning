# 数组里没有出现过的数字

# 给定一个长度为n的正整数数组nums，其中nums[i]的值都在区间[1,n]中，
# 请你找出nums数组在[1,n]范围内没有出现过的数组，并将其在数组中返回。

nums=[2,1,4,5,1,2]

def func(nums):
    maxnum = max(nums)
    length = len(nums)
    l = [i for i in range(1, length + 1)]
    l2 = []
    nums = set(nums) # 转成集合，元素不会重复
    for num in nums:
        if num in l:
            l.remove(num)

    print(l)
    return l

func(nums)
# 三个数的最大成绩

list = [-5,-1, 2, 3, 4, 4]

# 可能1:数组都是正数或者负数，就是最大的三个数相乘

# 可能2：有正有负，可能负负得正

# 两种情况都考虑

def func(list):
    list.sort()
    return max(list[0]*list[1]*list[-1],list[-1]*list[-2]*list[-3])

print(func(list))
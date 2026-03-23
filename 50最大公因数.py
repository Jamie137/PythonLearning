# 最大公因数

# 求两个数的最大公因数

# 方法1：
# 枚举法
def func1(a, b):
    if a == b:
        return a
    num = min(a,b)
    while a % num != 0 or b % num != 0:
        num -= 1
    return num

print(func1(12, 18))

# 方法2：
def func2(a, b):
    while b!= 0 :
        a, b = b, a%b
    return a

print(func2(12,18))
# 2的幂

# 非负数n，判断是否存在x使2^x= n

def func(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            return False
        
    return True
print(func(1))

# 位运算
# 0100(4)  1000(8)
# 0011(3)  0111(7)

# 一个数和他小一的数 做与运算是0
def func(n):
    tmp = bin(n)[2:]
    if tmp.count(1) == 1:
        return True
    
def func(n):
    return n>0 and n & (n-1) == 0

# 水仙花数

# 是一个三位数，各位数字立方和等于该数字本身

for i in range(1, 10):
    for j in range(0, 10):
        for o in range(0, 10):
            sumnum = i**3 + j**3 + o**3
            num = i * 100 + j * 10 + o
            if sumnum == num:
                print(num)


# n = 567
# a = n % 10
# b = (n % 100) // 10
# c = n // 100
def checknum(num):
    a = num % 10
    b = (num % 100) // 10
    c = num // 100
    if num == a**3 + b**3 + c**3:
        return True
    else:
        return False
for i in range(100, 1000):
    if checknum(i):
        print(i)
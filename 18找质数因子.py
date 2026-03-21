# 找质数因子
# 质分解，分解质因数
# 输入一个正整数，输出它的所有质数因子

# 先找所有因子列表
def getYinzi(a):
    list_yinzi = []
    for i in range(1, a):
        if a % i == 0:
            list_yinzi.append(i)
    return list_yinzi

# 判断质数
def checkPrime(num):
    flag = True
    if num == 1:
        flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag

a = int(input('请输入一个自然数：'))
l = getYinzi(a)

for i in l:
    if checkPrime(i):
        print(f'{i}是{a}的质数因子')


# 质分解
a = int(input('请输入一个自然数：'))
y = 2
list = []
while a >= y:
    if a % y == 0:
        list.append(y)
        a = a / y
    else:
        y = y + 1

print(list)

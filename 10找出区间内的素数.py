# 找出区间内的素数

# 输入整数a, b表示一个闭区间，找出该区间内所有素数
import math
a, b = map(int, input("请输入区间端点，以空格隔开").split())

for i in range(a, b + 1):
    flag = True
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)


def prime(n):
    flag = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag
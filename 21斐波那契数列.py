# 斐波那契数列

# 找出斐波那契数列的第n个项：1，1，2，3，5，8，13，21

n = int(input())
list = [1, 1]

for i in range(n):
    list.append(list[-1]+ list[-2])

print(list[n-1])

# 递归
# 终止条件
def fbnq(n):
    if n == 1 or n == 2:
        return 1
    while n >= 0:
        return fbnq(n-1) + fbnq(n - 2)
    
print(fbnq(4))

# 非递归
n = 6
fibs = [1, 1]
for i in range(2, n + 1):
    fibs.append(fibs[i-1] + fibs[i-2]) 

print(fibs)

    
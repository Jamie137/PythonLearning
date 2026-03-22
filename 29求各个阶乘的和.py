# 求各个阶乘的和

# 求1到20的阶乘的和

# 直接算
def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n-1)
    
res = 0
for i in range(1, 21):
    res += jiecheng(i)

print(res)

# 用math 模块

import math

sum = 0

for i in range(1,21):
    sum += math.factorial(i)

print(sum)
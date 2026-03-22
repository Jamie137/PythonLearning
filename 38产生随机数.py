# 生成随机数

import random

a = random.random()  # 左闭右开 0,1范围内

b = random.randint(1, 10)  #左闭右闭

C = random.randrange(1, 10, 3)  # 1和10之间，以3为步长取随机数

print(a,b, C)
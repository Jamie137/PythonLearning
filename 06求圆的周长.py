# 求圆的周长

# 给出半径求圆的周长
# 圆的周长C = 2ΠR = ΠD

import math
def circlelen(num):
    return 2 * math.pi * num

print('请输入圆的半径：')
num = float(input())
print(f'圆的周长为：{circlelen(num)}')
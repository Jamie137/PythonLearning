# 求圆的面积

pi = 3.14
def calculateS(r):
    return pi * r * r

r = float(input('请输入半径：'))
S = calculateS(r)
print(f'圆的面积为：{S}')
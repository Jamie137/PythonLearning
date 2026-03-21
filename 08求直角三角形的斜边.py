# 求直角三角形的斜边
# 输入两个直角边，求斜边
import math
x, y = map(float, input('请输入两个直角边，以空格隔开:').split())

z = math.sqrt(x*x + y * y)

print(f'斜边为{z}')
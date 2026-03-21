# 海伦公式求三角形面积
import math
a, b, c = map(int, input('请输入三角形三条边，以空格隔开：').split())

def getS(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S

print('三角形的面积是%.2f' % getS(a, b, c))
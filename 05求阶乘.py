# 求阶乘
# 编写程序，求出某个自然数的阶乘

# 方法一：非递归
def calculate(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

print('请输入需要求阶乘的自然数：')
num = int(input())
res = calculate(num)
print(f'{num} 的阶乘是 {res}')

# 方法二：递归

def diguicalculate(num):
    if num - 1 > 0:
        return num * diguicalculate(num-1)
    else:
        return num
print('递归数字：')
num = int(input())
print(diguicalculate(num))

# 教程方法

def jiecheng(num):
    if num == 1:
        return 1
    else:
        return num * jiecheng(num - 1)
    
print(jiecheng(5))
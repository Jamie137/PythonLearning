# 判断素数

def check(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag

print("请输入数字：")
num = int(input())

if check(num):
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')

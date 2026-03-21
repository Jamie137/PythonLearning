# 反向输出四位数

num = list(input())
num_l = reversed(num)
for i in num_l:
    print(i,end='')


a = int(input('请输入这个数：'))

a = str(a)

a = a[::-1]

print(int(a))
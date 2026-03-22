# 年龄急转弯

# 有5个人坐在一起，问第五个人多少岁？他说比第四个人大2岁，都比前一个人
# 大两岁，第一个人是10岁，第五个人多大


age = 10
for i in range(4):
    age += 2

print(age)


# 递归
def func(n):
    if n == 1:
        return 10
    else:
        return func(n-1) + 2
    
print(func(5))
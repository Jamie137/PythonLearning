# 变量值互换

a = 1
b = 2

# 方法1
a, b = b,a
print(a,b)


# 方法2
temp = a
a = b
b = temp
print(a,b)
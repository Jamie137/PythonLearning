# 替换空格

# 将字符串中的空格替换为'%'

x = input()
def func(x):
    res = ''
    for i in x:
        if i != ' ':
            res += i
        else:
            res += '%'
    return res
x = func(x)
# x.replace(' ', '%', len(x)) replace不会修改原字符串，只是返回一个新字符串
print(x)
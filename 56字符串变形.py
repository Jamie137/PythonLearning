# 字符串变形

# "Hello World"变形为"wORLD hELLO"

def func(s):
    l = s.split()
    l = l[::-1]
    s = ''
    for i in l:
        i = i.swapcase()
        s += i
        s += " "
    return s[0:len(s)-1]

print(func('Hello World'))
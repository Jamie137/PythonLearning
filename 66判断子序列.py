# 判断子序列

def func(a, b):
    if len(a) >= len(b):
        return False
    c = ''
    n = 0

    for i in b:
        if i == a[n]:
            n += 1
            c += i
    if a == c:
        return True
    return False

print(func('hlo','hello'))
    
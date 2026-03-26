# 字符串的相邻字符去重

def func(strs: str):
    tmp = ''
    for i, j in enumerate(strs):
        if not tmp or tmp[-1] != j:
            tmp += j
        else:
            tmp = tmp[:-1]
    return tmp

print(func('acbbc'))

    


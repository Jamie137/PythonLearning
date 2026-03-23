# 最长公共前缀

# 大小为n的字符串数组strs，包含n个字符串，编写一个函数来查找字符串数组中的最长公共前缀，返回这个公共前缀

l = ['abca', 'abc', 'abca', 'abc', 'abcc']
def func(l):
    n = len(l)
    if n == 0:
        return ''
    for i in range(len(l[0])):
        temp = l[0][i]
        for j in range(1, n):
            if i == len(l[j]) or temp != l[j][i]:
                 return l[0][0:i]
            
    return l[0]

print(func(l))
    # tmp = ''
    # for i in l:
    #     if tmp and i[]
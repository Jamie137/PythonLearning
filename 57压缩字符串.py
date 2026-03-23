# 压缩字符串

# aabcccccaaa变为a2bc5a3

a = input()
def func(a):
    dic  = dict()
    for i in a:
        if i in dic:
            dic[i] += 1


# ---

def func(s):
    list = []
    for i in s:
        if not list or list [-2] != i:
            list.append(i)
            list.append(1)
        else:
            list[-1] += 1

    return ''.join(map(str, [x for x in list if x !=1]))

print(func('aaabbccccddaa'))
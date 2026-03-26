# 移动0
# 给一个数组，把所有0移动到数组末尾，不改变其他顺序

def func(list):
    res = []
    tmp = []
    for i in list:
        if i == 0:
            tmp.append(0)
        else:
            res.append(i)
    res.extend(tmp)
    return res

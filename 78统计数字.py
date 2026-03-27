# 统计数字

def func(k: int, n: int):
    count = 0
    for i in range(0, n+1):
        times = str(i).count(str(k))
        count += times
    return count

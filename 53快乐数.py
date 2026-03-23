# 快乐数
# 给定一个正整数，判断这个数是否是快乐数
# 给定一个正整数，每次把他替换为他每个位置上的数字的平方和，如果这个数能变为1则是快乐数


num = int(input())


def func(num):
    x = list(map(int,list(str(num))))
    res = 0
    for i in x:
        res += i**2
    if res == 1:
        return True
    if res < 9:
        return False
    else:
        return func(res)
    
if func(num):
    print('快乐')

# 求各位数平方和
def change(x):
    sum = 0
    while x > 0:
        j = x % 10
        sum += j*j
        x //= 10
    return sum

def happynumber(n):
    while n > 9:
        n =change(n)
    if n == 1:
        return True
    else:
        return False

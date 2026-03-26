# 旋转字符串

# 给定两个字符串A和B，如果能将A从中间某个位置分割为左右两部分字符串，并将左边的字符串移动到右边字符串后面组成字符串B时返回true


def func(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if (A[i:] + A[0:i])== B:
            return True
    return False

print(func('3412','1234'))

# B 在 A + A里面则一定可以？？？牛逼
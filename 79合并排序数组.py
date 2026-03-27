# 合并排序数组
# 双指针

def func(A: list, B: list)-> list:
    a = 0
    b = 0
    c = []
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            c.append(A[a])
            a += 1
        if B[b] < A[a]:
            c.append(B[b])
            b += 1
        else:
            c.append(A[a])
            c.append(B[b])
            a += 1
            b += 1
        while a < len(A):
            c.append(A[a])
            a += 1
        while b < len(B):
            c.append(B[b])
            b += 1
    return c


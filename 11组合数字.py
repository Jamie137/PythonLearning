# 组合数字

# 有四个数字，1，2，3，4，能组成多少个互不相同且无重复数字的三位数，各是多少？

for i in range(1, 5):
    for j in range(1, 5):
        for m in range(1, 5):
            if (i != j) and (i != m) and (j != m):
                print(f'{i}{j}{m}')
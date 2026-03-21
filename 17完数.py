# 完数

# 一个数恰好等于除了它以外的因子之和。找出1000以内的所有完数。

def getWanshu(a, b):
    # 找出[a, b]范围内的完数
    for i in range(a, b+1):
        list = [] # 新建一个列表存储该数的所有因数
        # 遍历范围内的所有数
        for o in range(1, i):
            # 找出该数的所有因数
            if i % o == 0:
                list.append(o)
        if sum(list) == i:
            print(f'{i}是完数')

a, b = map(int, input("请输入两个端点范围，以空格隔开：").split())
getWanshu(a,b)

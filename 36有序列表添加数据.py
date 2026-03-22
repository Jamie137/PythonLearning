# 有序列表添加数据

l = [1, 4, 7, 9 ,15, 20, 37, 50]
newdata = int(input('请输入要插入的数据：'))

for i, j in enumerate(l):
    if newdata < j:
        a = l[i:]
        b = l[0:i]
        b.append(newdata)
        b.extend(a)
        break

print(b)
# 求矩阵主对角线元素之和

a = []
sum = 0
for i in range(3):
    a.append([])
    for j in range(3):
        k = int(input('请输入数据：'))
        a[i].append(k)
        if j == i:
            sum += k

print(sum)
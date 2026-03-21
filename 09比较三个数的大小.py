# 比较三个数的大小

# 输入三个数，从小到大输出三个数


# a, b, c = map(int, input('请输入三个整数，以空格隔开: ').split())

l = map(int, input('请输入三个整数，以空格隔开: ').split())
l1 = sorted(l)
print(f'三个数字从小到大的顺序是：{l1[0]}, {l1[1]}，{l1[2]}')
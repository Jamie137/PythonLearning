# 找出100以内偶数

# 练习
count = 100
for i in range(100):
    if i % 2 == 0:
        print(i)

# 拓展
print("请输入检查范围的最大数。")
count = int(input())

print("请输入检查的类型，0为偶数，1为奇数。")
flag = int(input())
flag_bool = True if flag == 1 else False
for i in range(count):
    if flag_bool and i % 2 != 0:
        print(i)
    if not flag_bool and i % 2 == 0:
        print(i)
        
# 讲解
list = []
for i in range(1, 100):
    if i % 2 == 0:
        list.append(i)

print(list)
# 复制列表

# 将一个列表的数据复制到另一个列表

list = [1, 2, 3, 4]

list1 = list  # 浅复制
list[0] = 5
print(list[0])

import copy

list2 = copy.copy(list)

list[1] = 33

print(list2)
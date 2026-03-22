# 落体反弹问题

# 一球从100米高度自由落下，每次落地后反弹回原高度的一半，再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？

n = int(input())
height = 100
height_list = []
distance = 100
for i in range(n):
    height_list.append(height)
    height = height / 2

    distance = distance + 2 * height
    
print(height)
print(distance) 
print(height_list[n-1])
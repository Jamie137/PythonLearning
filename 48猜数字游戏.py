# 猜数字游戏

# 生成随机数
import random
answer = random.randint(1,100)


times = 7
print('游戏开始,请输入100以内整数(有7次机会)：')
while times != 0:
    num = int(input())
    if num < answer:
        print('你猜的偏小')
        times -=1
        continue
    if num > answer:
        print('你猜的偏大')
        times -=1
        continue
    else:
        print('猜中了！')
        break
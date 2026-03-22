# 温度转换

# 摄氏度转华氏度，华氏度转摄氏度
# 华氏温度 = 摄氏温度 * 1.8 + 32

a = int(input('摄氏度请按1，华氏度请按2'))

def trans(a):
    if a == 1:
        b = float(input('请输入摄氏度'))
        res = b * 1.8 + 32
        print(res)
        return
    else:
        b = float(input('请输入华氏度'))
        res = (b-32) / 1.8
        print(res)
        return
    
trans(a)
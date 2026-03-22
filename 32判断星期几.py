# 判断星期几

# 输入星期几的第一个字母来判断是星期几
# Sunday,satu, tues,th
a = input('请输入第一个字母：')

if a == "M":
    print('星期一')
elif a == "W":
    print('星期三')
elif a == "F":
    print('星期五')
elif a == "T":
    b = input('请输入第二个字母：')
    if b == 'u':
        print('是周二')
    elif b == 'h':
        print('是周四')
    else:
        print('输入错误')

elif a == 'S':
    b = input('请输入第二个字母')
    if b == 'u':
        print('星期日')
    elif b == 'a':
        print('星期六')
    else:
        print('输入错误')

else:
    print('输入错误')

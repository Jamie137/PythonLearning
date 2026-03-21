# 判断字母

a = input()
result = a.isalpha()
if result:
    print(f'{a}是字母')
else:
    print(f'{a}不是字母')

print(f'a的ASCII码为{ord(a)}')
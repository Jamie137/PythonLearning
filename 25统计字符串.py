# 统计字符

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

xxx = input('请输入字符串：')

char = 0
number = 0
space = 0
other = 0

for  i in xxx:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        number += 1
    elif i.isspace():
        space += 1
    else:
        other += 1

print(f'字母数量为{char},数字有{number}个，空格有{space}个，其他有{other}个')

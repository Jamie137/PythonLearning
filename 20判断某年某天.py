# 判断某年某天
# 输入某年某月某日，判断这一天是今年的第几天

import datetime

year , month, day = map(int, input("请输入年月日，以空格隔开").split())

yuandan = datetime.datetime(year, 1, 1)

now = datetime.datetime(year, month, day)

print((now - yuandan).days + 1)
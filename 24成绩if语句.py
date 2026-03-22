# 成绩if语句
score = int(input('请输入成绩：'))
def chengji(score):
    if score >= 90:
        print('A')
    elif score >=60:
        print('B')
    else:
        print('C')
chengji(score)
# 判断三角形

a, b, c = map(float, input('请输入三条边，以空格隔开:').split())
def checksanjiaoxing(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print('输入数据不合法')
        return False
    
    if a + b > c and a + c > b and b + c > a:
        print('这三条边可以是边长')
        return True
    else:
        print('不可以是三角形的三边')
        return False
    
checksanjiaoxing(a, b, c)
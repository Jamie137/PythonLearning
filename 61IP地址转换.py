# IP地址转换

# 把ip地址转换成一个整数
# '{:08b}'.format()
x = '114.55.207.244'

def func(x):
    x_l = x.split('.')

    s = ''
    for i in x_l:
        tmp = bin(int(i))[2:]
        tmp = tmp.rjust(8,'0')
        print(tmp)
        s += tmp

    print(int(s, 2))
func(x)
# 求指定数列和

# 分数序列：2/1, 3/2, 5/3, 8/5, 13/8, 21/13求这个数列前20项之和

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)
    
res = 0
for i in range(20):
    res += fib(i + 3)/fib(i + 2)

print("%.2f"% res)
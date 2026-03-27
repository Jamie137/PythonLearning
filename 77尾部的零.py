# 

def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n-1)
    
def func(n: int) -> int:
    num = str(jiecheng(n))
    count = 0
    for i in num[::-1]:
        if i == '0':
            count += 1
        else:
            return count
        
print(func(5))
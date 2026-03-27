# 柠檬水找零
# 贪心算法
def func(bills: list) -> bool:
    five_count = 0
    ten_count = 0
    twenty_count = 0
    for i in bills:
        if i == 5:
            five_count += 1
            continue
        if i == 10 and five_count > 0 :
            five_count -= 1
            ten_count += 1
            continue
        if i == 20:
            if five_count > 0 and ten_count > 0:
                five_count -= 1
                ten_count -= 1
                twenty_count += 1
                continue
            if five_count >= 3:
                five_count -= 3
                twenty_count += 1
                continue
        return False
    return True

print(func([5,5,5,10,20,20,5,5,5,10,20,20,20]))

print(func([5,5,10,5,20]))

print(func([10]))
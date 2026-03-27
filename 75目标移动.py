# 目标移动
# 双指针
def func(nums: list, target: str):
    count = 0
    left = len(nums) - 1
    right = len(nums) - 1
    while left >= 0:
        if nums[left] != target:
            print('不等')
            print(f'left:{left}')
            print(f'right:{right}')
            print(nums)
            nums[right] = nums[left]
            right -= 1
        else:
            print('相等')
            print(f'left:{left}')
            print(f'right:{right}')
            count += 1
        left -= 1
    for i in range(count):
        nums[i] = target
    print(nums)
func([1,1,2,1,3,4],1)
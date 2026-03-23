# 第一个只出现一次的字符

string = 'Hello World'
a = -1
mp = dict()

for i in string:
    if i in mp.keys():
        mp[i] += 1
    else:
        mp[i] = 1

for i in range(len(string)):
    if mp[string[i]] == 1:
        a = i
        break
print(a)
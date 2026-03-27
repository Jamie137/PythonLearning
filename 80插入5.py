def func(a: int)->int:
    string = ''
    ans = 0
    n = 0
    flag = False
    if a >= 0:
        string = str(a)
        n = len(string)
        for i in range(n):
            if (ord(string[i]) - ord('0') < 5) and flag == False:
                ans = ans * 10 + 5
                flag = True
            ans = ans * 10 + ord(string[i]) - ord('0')
        if not flag:
            ans = ans * 10 + 5
    else:
        a = -a
        string = str(a)
        n = len(string)
        for i in range(n):
            if ord(string[i]) - ord('0') > 5 and flag == False:
                ans = ans * 10 + 5
                flag = True
            ans = ans * 10 + ord(string[i]) - ord['0']
        if flag == False:
            ans = ans * 10 +5
        ans = -ans
    return ans

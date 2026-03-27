# 字符删除

def delete_str(strs: str, subs: str)-> str:
    res = ""
    # 先把sub转集合
    s = set(subs)
    for i in strs:
        if i in subs:
            continue
        else:
            res += i
    return res

# 이상한 문자 만들기

def solution(s):
    s = list(s)
    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            continue
        if idx&1: s[i] = s[i].lower()
        else: s[i] = s[i].upper()
        idx += 1
    return "".join(s)

print(solution('try hello world')) # 'TrY HeLlO WoRlD'
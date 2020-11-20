# 문자열 다루기 기본

def solution(s):
    if len(s)!=4 and len(s)!=6: return False
    for i in s:
        if i not in '1234567890': return False
    return True

print(solution('a234')) # false
print(solution('1234')) # true
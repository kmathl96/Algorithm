# 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    return s.count('p')==s.count('y')

print(solution('pPoooyY')) # true
print(solution('Pyy')) # false
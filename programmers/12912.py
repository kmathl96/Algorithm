# 두 정수 사이의 합

def solution(a, b):
    return sum(range(a if a<b else b, a+1 if a>=b else b+1))

print(solution(3,5)) # 12
print(solution(3,3)) # 3
print(solution(5,3)) # 12
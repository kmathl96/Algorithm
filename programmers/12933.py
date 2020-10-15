# 정수 내림차순으로 배치하기

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=1)))

print(solution(118372)) # 873211
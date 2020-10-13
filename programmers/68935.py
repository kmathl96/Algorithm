# 3진법 뒤집기
# 월간 코드 챌린지 시즌1

def solution(n):
    cnt = 0
    a = [] # 3진법으로 표현하는 수를 넣음
    while True:
        a.append(n%3)
        n = n//3
        cnt += 1
        if n==0: break
    return sum([a.pop()*(3**i) for i in range(len(a))])

print(solution(45)) # 7
print(solution(125)) # 229
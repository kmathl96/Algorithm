# 124 나라의 숫자

a = [1,2,4]

def solution(n):
    answer = ''
    while True:
        n -= 1
        answer = str(a[n%3]) + answer
        if n//3: n = n//3
        else: break
    return answer

for i in range(1,11):
    print(solution(i)) # 1,2,4,11,12,14,21,22,24,41
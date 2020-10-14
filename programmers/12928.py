# 약수의 합

def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if not n%i:
            answer += i
            if i**2 != n: answer += n//i
    return answer

print(solution(12)) # 28
print(solution(5)) # 6
# 피보나치 수

def solution(n):
    fibo = [0]*(n+1)
    fibo[1] = 1
    for i in range(2,n+1):
        fibo[i] = (fibo[i-2]+fibo[i-1])%1234567
    return fibo[n]

print(solution(3)) # 2
print(solution(5)) # 5
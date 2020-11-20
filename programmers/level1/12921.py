# 소수 찾기

def solution(n):
    prime = [2]
    for i in range(3,n+1,2):
        isPrime = True
        for p in prime:
            if p > i**0.5: break # 해당 숫자의 제곱근까지만 확인하면 됨
            if not i%p:
                isPrime = False
                break
        if isPrime: prime.append(i) # 한번도 소수로 나눠지지 않았을 경우 해당 숫자를 소수로 판단
    return len(prime)

print(solution(10)) # 4
print(solution(5)) # 3
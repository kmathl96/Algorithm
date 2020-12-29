# 골드바흐의 추측
# 소수를 판별하는 함수로 확인하면 시간초과
# 에라토스테네스의 체를 활용하여 미리 소수를 구해놓고 판별

# def f(num): # 소수 판별 함수
#     for i in range(2,int(num**0.5)+1):
#         if num%i == 0: return False
#     return True

# 에라토스테네스의 체를 활용하여 소수 리스트 구하기
primes = [1]*1000001
primes[0],primes[1] = 0,0
for i in range(3,1000000):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            primes[i] = 0
            break

while True:
    n = int(input())
    if n == 0: break
    ans = "Goldbach's conjecture is wrong."
    for num in range(3,n//2+1,2):
        if primes[num] and primes[n-num]:
            ans = f'{n} = {num} + {n-num}'
            break
    print(ans)
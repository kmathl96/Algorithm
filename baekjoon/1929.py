# 소수 구하기
# 수학, 정수론, 소수 판정, 에라토스테네스의 체

M,N = map(int,input().split()) # M 이상 N 이하의 소수 구하기
primes = [1]*(N+1) # 소수 여부
primes[1] = 0 # 1은 소수가 아님
for i in range(2,int(N**0.5)+1):
    if not primes[i]: continue # 소수가 아니면 넘어감

    # i의 배수는 소수가 아님
    for j in range(i*2,N+1,i):
        primes[j] = 0

# M 이상 N 이하의 소수를 한 줄에 하나씩 순서대로 출력
print('\n'.join(map(str,[i for i in range(M,N+1) if primes[i]])))
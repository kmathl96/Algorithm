# 소수의 연속합
# 수학, 정수론, 투 포인터, 소수 판정, 에라토스테네스의 체

N = int(input()) # 연속된 소수의 합으로 나타내고자 하는 수

isPrime = [1]*(N+1) # 소수 여부
for i in range(2,int(N**0.5)+1): # N의 제곱근보다 큰 최소 정수까지만 확인하면 됨
    if isPrime[i]: # 소수인 경우
        # 해당 수의 배수인 수들은 소수가 아니므로 변경
        for j in range(2*i,N+1,i):
            isPrime[j] = 0
primes = [num for num in range(2,N+1) if isPrime[num]] # 소수

answer = 0 # N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수
M = len(primes) # N 이하의 소수의 개수
if M: # N 이하의 소수가 있는 경우
    i,j = 0,1 # 구간 [i,j)의 양 끝 포인터
    sub_sum = primes[0] # 구간의 합
    while True:
        # 합이 N 이상인 경우, 왼쪽 포인터 이동 및 구간 합 갱신
        if sub_sum >= N:
            # 구간 합이 N과 같다면 answer 증가
            if sub_sum == N: answer += 1
            sub_sum -= primes[i]
            i += 1
        
        # j가 끝에 도달한 경우, 더 확인할 필요가 없으므로 종료
        elif j == M: break

        # 그 외의 경우, 오른쪽 포인터를 이동하고 구간 합 갱신
        else:
            sub_sum += primes[j]
            j += 1
print(answer)
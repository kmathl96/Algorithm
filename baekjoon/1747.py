# 소수&팰린드롬
# 수학, 브루트포스, 정수론, 소수 판정, 에라토스테네스의 체

# N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수 구하기
N = int(input())

mx = 1003001 # N이 최댓값(1000000)일 떄의 답

# 소수 여부 판단
primes = [1]*(mx+1) # 0~1003001의 소수 여부
primes[1] = 0 # 1은 소수가 아님
for num in range(2,int(mx**0.5)+1):
    # 소수가 아닌 경우 넘어감
    if not primes[num]: continue

    # num의 배수들은 소수가 아니므로 소수 여부를 0으로 변경
    for i in range(2*num,mx,num):
        primes[i] = 0

# 소수가 아니거나 팰린드롬이 아닌 경우 N을 증가시키면서 답을 찾기
while not primes[N] or str(N)!=str(N)[::-1]:
    N += 1

print(N)
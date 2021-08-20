# 동전 2
# 다이나믹 프로그래밍

n,k = map(int,input().split()) # 동전의 종류 수, 만들 가치
coins = list(set(int(input()) for _ in range(n))) # 동전의 가치 (중복 제거)

dp = [10001]*(k+1) # dp[i] : i원을 만들 수 있는 동전의 최소 개수
dp[0] = 0
for coin in coins:
    for i in range(coin,k+1):
        # (i-coin)원애 coin원을 더하는 경우의 최소 개수 = dp[i-coin]+1
        dp[i] = min(dp[i],dp[i-coin]+1)

# k원을 만들 수 있는 동전의 최소 개수 출력
# 불가능한 경우(= 초기 값과 같은 경우), -1 출력
print(-1 if dp[k] == 10001 else dp[k])
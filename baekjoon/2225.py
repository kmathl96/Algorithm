# 합분해
# 다이나믹 프로그래밍

N,K = map(int,input().split())

# dp[i] = i를 만들기 위한 경우의 수
# K-1번 갱신하여 K개로 만들 수 있는 경우의 수를 구함
dp = [1]*(N+1) # 1개로 i를 만들 수 있는 경우의 수는 1이므로 모두 1로 초기화
for _ in range(K-1): 
    for i in range(1,N+1):
        dp[i] += dp[i-1]
print(dp[N]%1000000000)
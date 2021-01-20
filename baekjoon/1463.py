# 1로 만들기
# 다이나믹 프로그래밍

N = int(input())
# dp[i] : i을 1로 만드는 데 필요한 연산의 최소 횟수
dp = [1000000]*(N+1) # N의 최댓값이 10^6이므로 10^6으로 초기화
dp[1] = 0 # N=1인 경우 최솟값이 0이므로 0으로 초기화
for i in range(2,N+1):
    if not i%3: dp[i] = dp[i//3]+1
    if not i%2 and dp[i] > dp[i//2]+1: dp[i] = dp[i//2]+1
    if dp[i] > dp[i-1]+1: dp[i] = dp[i-1]+1
print(dp[N])
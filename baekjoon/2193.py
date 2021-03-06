# 이친수
# 다이나믹 프로그래밍

N = int(input())
dp = [0]*(N+1)
dp[1] = 1 # 한 자리 이친수의 개수는 1로 초기화
for i in range(2,N+1):
    # i-1 자리 이친수 중에서
    # 0을 붙일 수 있는 경우는 i-1 자리 이친수 모두 해당하므로, dp[i-1]의 개수를 가짐
    # 1을 붙일 수 있는 경우는 i-1 자리 이친수 중 0으로 끝나는 수이고,
    # 즉 i-2 자리 이친수에 0을 붙여서 만들어진 이친수이므로, dp[i-2]의 개수를 가짐
    dp[i] = dp[i-1] + dp[i-2] # i-1 자리 이친수에 0을 붙이는 경우의 수 + 1을 붙이는 경우의 수
print(dp[N])
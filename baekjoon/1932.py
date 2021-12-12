# 정수 삼각형

n = int(input()) # 삼각형의 크기

# dp[i][j] : 삼각형의 i번째 줄 j번째 요소까지 더한 경우의 제일 큰 값
# = (이전 행(i-1)의 이전 열(j-1)과 현재 열(j) 중 큰 값) + 해당 요소의 값
# dp의 크기를 (n+1)*(n+1)로 두고, 첫 행과 첫 열의 값은 전부 0으로 함
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    row = list(map(int,input().split())) # 정수 삼각형의 한 줄
    for j in range(len(row)):
        dp[i+1][j+1] = max(dp[i][j],dp[i][j+1])+row[j]
print(max(dp[n])) # 마지막 줄까지 더했을 때의 값들 중 최댓값
# RGB거리 2
# 다이나믹 프로그래밍

N = int(input()) # 집의 수
cost = [list(map(int,input().split())) for _ in range(N)] # 집을 칠하는 비용
dp = [[0]*3 for _ in range(N)] # dp[i][j] : i번 집을 j색으로 칠했을 때의 최소 비용
answer = 1000000 # 비용의 최댓값으로 초기화

# 1번 집을 칠하는 색에 따라 마지막 집에 칠할 수 있는 색이 다름
for first_color in range(3):
    
    # dp 초기화 : 1번 집은 first_color로 칠함
    for j in range(3):
        # 1번 집을 칠한 색깔만 dp에 해당 비용을 저장
        if j==first_color: dp[0][j] = cost[0][j]
        # 다른 색깔은 선택하지 않도록 비용의 최댓값을 저장
        else: dp[0][j] = 1001
    
    # 2번 집부터 마지막 집까지
    # 규칙을 만족하면서 칠하는 경우의 최소 비용 저장
    for i in range(1,N):
        for j in range(3):
            # ((i-1)번 집을 j색으로 칠하지 않은 경우 중 최소 비용) + i번 집을 j색으로 칠하는 비용
            dp[i][j] = min(dp[i-1][k] for k in range(3) if j!=k)+cost[i][j]
    
    # 마지막 집까지 칠하는 경우의 최소 비용을 answer에 저장
    for i in range(3):
        # 1번 집과 같은 색을 칠한 경우는 제외
        if i != first_color and answer > dp[N-1][i]: answer = dp[N-1][i]
print(answer)
# RGB거리
# 다이나믹 프로그래밍

N = int(input()) # 집의 수
cost = [list(map(int,input().split())) for _ in range(N)] # 각 집을 빨강, 초록, 파랑으로 칠하는 비용

for i in range(1,N): # i번째 집까지 칠하는 데 든 총 비용 계산
    for j in range(3): # 색깔별로 비용 저장
        # 이전 집까지 칠하는 데 들었던 비용(cost[i-1][k]) 중에서
        # 해당 색깔이 아닌 경우(k!=j)들의 최소 비용을
        # 이번 집을 해당 색깔로 칠하는 비용(cost[i][j])에 더함
        cost[i][j] += min(cost[i-1][k] for k in range(3) if k!=j)
print(min(cost[N-1])) # 마지막 집까지 칠하는 비용의 최솟값
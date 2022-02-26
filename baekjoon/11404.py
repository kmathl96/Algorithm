# 플로이드
# 플로이드-와샬

import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
cost = [[10000000]*n for _ in range(n)] # cost[i][j] = i->j 이동 비용

# 버스의 정보에 따라 비용 저장
for _ in range(m):
    # 시작 도시, 도착 도시, 한 번 타는 데 필요한 비용
    a,b,c = map(int,input().split())

    # 두 도시를 연결하는 노선은 하나가 아닐 수 있으므로 더 작은 값을 저장
    cost[a-1][b-1] = min(cost[a-1][b-1],c)

# 플로이드-와샬
for k in range(n):
    cost[k][k] = 0 # 같은 도시를 가는 비용은 0
    for i in range(n):
        for j in range(n):
            # i->j 경로와 i->k->j 경로 중 더 작은 비용 저장
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])

# i->j 경로가 존재하지 않는 경우는 0 출력
for i in range(n):
    for j in range(n):
        # 초기화했던 값과 같다면 경로가 존재하지 않는 것임
        if cost[i][j]==10000000:
            cost[i][j] = 0

# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값 출력
for row in cost:
    print(*row)
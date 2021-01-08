# 연결 요소의 개수
# 그래프와 BFS

from collections import deque

N,M = map(int,input().split())
adj = [[0]*(N+1) for _ in range(N+1)] # 인접한 정점들을 표시하기 위한 행렬
for _ in range(M):
    u,v = map(int,input().split())
    adj[u][v],adj[v][u] = 1,1 # 방향이 없으므로 u-v, v-u 둘 다 표시
visited = [0]*(N+1) # 정점을 방문했는지 확인하기 위한 리스트
ans = 0
for i in range(1,N+1):
    if visited[i]: continue # 이미 방문한 정점이면 통과
    q = deque([i])
    visited[i] = 1
    while q:
        cur = q.pop()
        for j in range(1,N+1):
            # 이미 방문했거나 연결돼 있지 않다면 통과
            if visited[j] or not adj[cur][j]: continue
            visited[j] = 1
            q.append(j) # 해당 정점에서도 연결된 정점들 찾기 위해 q에 넣음
    ans += 1
print(ans)
# DFS와 BFS
# 그래프와 BFS

from collections import deque

def dfs(v):
    ans1.append(v)
    for i in range(1,N+1):
        if adj[v][i] and i not in ans1: dfs(i)

def bfs(v):
    q = deque([v])
    while q:
        cur = q.popleft()
        for i in range(1,N+1):
            if adj[cur][i] and i not in ans2:
                q.append(i)
                ans2.append(i)

N,M,V = map(int,input().split())
adj = [[0]*(N+1) for _ in range(N+1)] # 인접 행렬
lines = [list(map(int,input().split())) for _ in range(M)]
for a,b in lines:
    adj[a][b],adj[b][a] = 1,1
ans1,ans2 = [],[V]
dfs(V)
bfs(V)
print(*ans1)
print(*ans2)
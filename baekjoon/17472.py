# 다리 만들기 2
# 그래프, 브루트포스, BFS, DFS, 최소 스패닝 트리(MST)

from collections import deque

# Kruskal
# 해당 섬(노드)의 부모 노드를 반환
def find_set(x):
    if p[x] != x: p[x] = find_set(p[x])
    return p[x]

# 두 섬(노드)의 부모 노드를 비교, 처리하여 두 섬을 이어줌
def union(x,y):
    px,py = find_set(x),find_set(y)
    if rank[px] > rank[py]: p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]: rank[py] += 1

# BFS로 섬 찾으면서 몇 번째 섬인지 표시
# 모든 섬이 1로 초기화 돼있으므로 V(2로 초기화)를 이용하여 2부터 표시
# 마지막 섬 표시하고 V 하나 커지므로 섬의 개수 = V-2
dr,dc = [-1,0,1,0],[0,1,0,-1]
def find_island(row,col):
    global mp
    q = deque([(row,col)])
    mp[row][col] = V
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<N and 0<=nc<M and mp[nr][nc]==1:
                mp[nr][nc] = V
                q.append((nr,nc))

# 놓을 수 있는 다리(섬1, 섬2, 다리 길이) 구하기
def find_edges(row,col):
    global edges
    for i in range(4):
        nr,nc = row+dr[i],col+dc[i]
        while 0<=nr<N and 0<=nc<M:
            # 자신의 값과 같으면 탐색 종료
            if mp[nr][nc] == mp[row][col]: break
            # 자신의 값과 다른, 0이 아닌 값을 발견
            if mp[nr][nc]:
                # 놓을 수 있는 다리의 길이
                # 같은 행이면 row-nr=0 => diff = 열 차이
                # 같은 열이면 col-nc=0 => diff = 행 차이
                diff = abs(row-nr+col-nc)-1
                # 다리의 길이가 1보다 크고, 해당 다리가 아직 edges에 있지 않는 경우에 추가
                if diff > 1 and (mp[nr][nc],mp[row][col],diff) not in edges:
                    edges.add((mp[row][col],mp[nr][nc],diff))
                break # 더 탐색하지 않으므로 종료
            # 0인 경우 해당 방향으로 탐색 반복
            nr += dr[i]
            nc += dc[i]

N,M = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(N)]
edges = set()
V = 2 # 섬이 1로 표시돼 있으므로 2로 초기화하여 1씩 증가시키면서 표시

# 섬을 찾고 몇 번째 섬인지 표시
for r in range(N):
    for c in range(M):
        if mp[r][c]==1:
            find_island(r,c)
            V += 1 # 다음 섬에 표시하기 위해 증가

# 다리를 놓을 수 있는 경우와 그 다리 길이를 찾음
for r in range(N):
    for c in range(M):
        if mp[r][c]: find_edges(r,c)

ans,cnt = 0,0 # 다리 길이의 총합, 다리의 개수
p = list(range(V))
rank = [0]*(V)
for v1,v2,w in sorted(list(edges), key=lambda x: x[2]): # 다리 길이가 짧은 것부터 고려
    if find_set(v1) == find_set(v2): continue # 두 섬의 부모 노드가 같다면 이어져 있다는 의미이므로 넘어감
    union(v1,v2) # 두 섬을 이음
    ans += w # 총 다리 길이에 더함
    cnt += 1 # 다리 개수 증가
    if cnt == V-3: break # 다리 개수가 섬의 개수(V-2)-1과 같아지면 종료 
print(-1 if cnt < V-3 else ans) # 섬을 다 잇지 못한 경우 -1 출력
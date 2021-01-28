# 상근이의 여행
# 최소 신장 트리

import sys # input()은 시간 초과나므로 sys.stdin.readline() 이용

### 1 ###
# 중복 방문 허용하며 비행기의 종류의 개수를 구하는 것이므로
# N개국을 가려면 최소 N-1 종류의 비행기를 타야 함
for _ in range(int(input())):
    N,M = map(int,input().split())
    for i in range(M):
        sys.stdin.readline()
    print(N-1)

### 2 ###
# 크루스칼 이용
def find_set(x): # 루트 구함
    if p[x] != x: p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    px,py = find_set(x),find_set(y)
    # x의 루트가 y의 루트보다 높을 때 x의 루트를 y 루트의 부모로 저장
    if rank[px] > rank[py]: p[py] = px
    else: # 위와 반대의 경우이거나 동등할 경우
        p[px] = py # 반대로 저장
        if rank[px]==rank[py]: rank[py]+=1 # 동등한 경우에는 한쪽을 높여줌

for _ in range(int(input())):
    N,M = map(int,input().split())
    edges = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
    p = list(range(N+1)) # 부모 저장
    rank = [0]*(N+1) # 트리의 높이
    ans = 0
    for v1,v2 in edges:
        # 두 정점의 루트가 같다면 이미 방문한 것이므로 넘어감
        if find_set(v1)==find_set(v2): continue
        # 아닌 경우, 이어줌 (해당 비행기를 탐)
        union(v1,v2)
        ans += 1
    print(ans)

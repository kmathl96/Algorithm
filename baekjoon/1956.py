# 운동
# 플로이드-와샬

V,E = map(int,input().split()) # 마을과 도로의 개수
inf = float('INF')

# edges[i][j] = i번 마을에서 j번 마을로 가는 도로의 길이
edges = [[inf]*V for _ in range(V)]
for _ in range(E):
    # a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있음
    a,b,c = map(int,input().split())
    edges[a-1][b-1] = c

# 각 마을로 가는 최단 거리 구하기
for k in range(V):
    # k를 통해서 i에서 j로 가는 도로의 길이 갱신
    for i in range(V):
        # i->k 경로가 없다면 넘어감
        if edges[i][k]==inf: continue
        # i->j 거리와 i->k->j 거리를 비교하여 작은 값 저장
        for j in range(V):
            edges[i][j] = min(edges[i][j],edges[i][k]+edges[k][j])

# 최소 사이클의 도로 길이의 합 구하기
# 자기 자신으로 오는 경로의 도로 길이 중 최솟값
ans = min(edges[r][r] for r in range(V))
# ans가 inf 값인 경우, 운동 경로를 찾는 것이 불가능하므로 -1 출력
print(ans if ans!=inf else -1)
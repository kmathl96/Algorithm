# 특정한 최단 경로
# 다익스트라

import sys,heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [inf]*N # start 정점에서부터의 거리
    dist[start] = 0
    q = [(0,start)] # 최소 힙 : (거리, 정점 번호)
    while q:
        d,cur = heapq.heappop(q) # 현재 정점과의 거리와 정점 번호

        # 저장되어 있는 값보다 큰 경우, 더 갱신할 필요가 없으므로 넘어감
        if d > dist[cur]: continue

        # 연결되어 있는 정점 탐색
        for node,w in graph[cur]:
            # cur 정점을 지나가는 경우가 더 거리가 짧다면 갱신
            if d+w < dist[node]:
                dist[node] = d+w # start-cur 거리와 cur-node 거리 더한 값 저장
                heapq.heappush(q,(d+w,node)) # 힙에 넣기
    
    return dist # 거리 리스트 반환

N,E = map(int,input().split()) # 정점의 개수와 간선의 개수
graph = [[] for _ in range(N)]
for _ in range(E):
    # a번 정점에서 b번 정점까지 거리가 c인 양방향 길 존재
    a,b,c = map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))
v1,v2 = map(lambda x: int(x)-1,input().split()) # 반드시 거쳐야 하는 두 개의 정점 번호
inf = float('INF')

# 두 개의 정점(v1,v2)를 지나는 최단 경로의 길이 구하기
dists = [dijkstra(0),dijkstra(v1),dijkstra(v2)] # 0,v1,v2에서부터 각 장점과의 거리
# 시작점-v1-v2-마지막점, 시작점-v2-v1-마지막점 경로 중 더 작은 값 저장
ans = min(dists[0][v1]+dists[1][v2]+dists[2][N-1],dists[0][v2]+dists[2][v1]+dists[1][N-1])
print(ans if ans!=inf else -1) # 그러한 경로가 없는 경우, -1 출력
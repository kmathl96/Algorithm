# 특정 거리의 도시 찾기
# 다익스트라

import sys,heapq
input = sys.stdin.readline

def dijkstra():
    dist = [300000]*(N+1) # 도시 X와의 거리
    dist[X] = 0
    q = [(0,X)] # 최소 힙
    while q:
        d,cur = heapq.heappop(q) # 거리, 도시
        # 저장되어 있는 거리보다 큰 경우, 갱신할 필요가 없음
        if d > dist[cur]: continue

        # 연결되어 있는 도시 탐색
        for node in graph[cur]:
            # 현재 도시를 거쳐가는 경우가 더 짧은 경우
            if dist[node] > d+1:
                dist[node] = d+1 # 최단 거리 갱신
                heapq.heappush(q,(d+1,node)) # 힙에 넣기
    
    # X에서 각 도시로 가는 최단 거리를 반환
    return dist

N,M,K,X = map(int,input().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호

# 도로 정보 저장하기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split()) # A번 도시에서 B번 도시로 이동하는 단방향 도로 존재
    graph[A].append(B)

dist = dijkstra() # 도시 X와 각 도시와의 최단 거리

# X로부터 출발하여 도달할 수 있는 도시 중에서,
# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
ans = [i for i in range(1,N+1) if dist[i]==K] # 거리가 K인 도시의 번호 저장
if not ans: ans.append(-1) # 하나도 존재하지 않는 경우 -1 넣기
for node in ans: print(node)
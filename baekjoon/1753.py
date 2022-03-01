# 최단경로
# 다익스트라

import sys,heapq
input = sys.stdin.readline

V,E = map(int,input().split()) # 정점의 개수, 간선의 개수
K = int(input()) # 시작 정점의 번호

# 간선 배열에 간선 정보 저장
# edges = [[0]*V for _ in range(V)] # 메모리 초과
edges = [[] for _ in range(V)] # 간선 배열
for _ in range(E):
    u,v,w = map(int,input().split()) # u에서 v로 가는 가중치 w인 간선
    edges[u-1].append((v-1,w)) # 간선 배열에 (도착점, 가중치)를 넣음

inf = float('INF')
dist = [inf]*V # 시작 정점으로부터의 거리
dist[K-1] = 0 # 시작 정점은 0으로 변경

# 최단 경로 구하기
# 최소 힙을 이용해 가중치가 최소인 간선부터 고려
q = [(0,K-1)] # 힙 : (정점까지의 거리,정점의 번호)
while q:
    d,cur = heapq.heappop(q) # 현재 정점까지의 거리와 번호

    # 저장된 거리보다 큰 경우, 갱신할 필요가 없으므로 넘어감
    if dist[cur] < d: continue

    # 현재 정점과 연결된 정점의 번호와 가중치
    for i,w in edges[cur]:
        # 현재 정점과 해당 정점(i)과 연결할 때의 거리(d+w)가
        # 해당 정점까지의 거리(dist[i])보다 작은 경우
        if d+w < dist[i]:
            dist[i] = d+w # 연결된 정점과의 거리 갱신
            heapq.heappush(q,(d+w,i)) # 힙에 해당 정점의 정보 넣기

# 각 정점으로의 최단 경로의 경로값(경로가 존재하지 않는 경우에는 INF)을 출력
for d in dist:
    print(d if d!=inf else 'INF')
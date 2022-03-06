# 미확인 도착지
# 다익스트라

import sys,heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [2000000]*(n+1) # 출발지와의 최단 거리
    dist[start] = 0
    q = [(0,start)] # 최소 힙
    while q:
        d,cur = heapq.heappop(q) # 거리, 현재 교차로

        # 최단 거리보다 크다면 넘어감
        if dist[cur] < d: continue

        # 도로로 연결되어 있는 교차로 탐색
        for node,nd in graph[cur]:
            # 저장되어 있는 최단 거리보다 현재 교차로를 거쳐서 가는 경로의 거리가 더 작은 경우
            if dist[node] > d+nd:
                dist[node] = d+nd # 최단 거리 갱신
                heapq.heappush(q,(d+nd,node)) # 더 탐색하기 위해 힙에 넣기
    return dist

T = int(input()) # 테스트 케이스의 개수
answer = []
for _ in range(T):
    n,m,t = map(int,input().split()) # 교차로, 도로, 목적지 후보의 개수
    s,g,h = map(int,input().split()) # 예술가들의 출발지, 지나간 두 개의 교차로 (g-h 도로를 지남)
    
    # 도로 정보 저장하기
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        # a와 b 사이에 길이 d의 양방향 도로가 있음
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    
    cand = [int(input()) for _ in range(t)] # 목적지 후보들

    # 출발지와 경유지들에서 각 교차로로 가는 최단 거리
    distS,distG,distH = dijkstra(s),dijkstra(g),dijkstra(h)

    # 목적지 후보들 중 불가능한 경우들을 제외한 목적지들을 구해, 오름차순으로 정렬
    # => 출발지에서 목적지까지의 최단 거리가 g와 h를 거쳐가는 경로의 거리와 같은 경우, 목적지일 가능성이 있음
    answer.append(sorted([e for e in cand if distS[e] in (distS[g]+distG[h]+distH[e],distS[h]+distH[g]+distG[e])]))

# 
for ans in answer: print(*ans)
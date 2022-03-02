# 파티
# 다익스트라

import sys,heapq
input = sys.stdin.readline

def dijkstra(road):
    dist = [100000]*N # X로 가는/오는 데 걸리는 소요 시간
    dist[X-1] = 0 # X는 0으로 변경
    q = [(0,X-1)] # 최소 힙 : (소요 시간, 마을 번호)
    while q:
        w,cur = heapq.heappop(q)

        # 소요 시간보다 크면 더 탐색할 필요가 없으므로 넘어감
        if w > dist[cur]: continue

        # 연결된 마을들 탐색
        for node,time in road[cur]:
            # 저장되어 있는 소요시간보다 cur을 거쳐서 가는 시간이 더 작은 경우
            if w+time < dist[node]:
                dist[node] = w+time # 최단 소요 시간 갱신
                heapq.heappush(q,(w+time,node)) # 더 탐색하기 위해 힙에 넣기
    return dist

N,M,X = map(int,input().split()) # 학생의 수, 도로의 수, 파티를 벌이는 마을의 번호
go = [[] for _ in range(N)] # 가는 방향의 그래프
come = [[] for _ in range(N)] # 오는 방향의 그래프
for _ in range(M):
    s,e,t = map(int,input().split()) # 도로의 시작점, 끝점, 도로를 지나는 데 필요한 소요 시간
    go[s-1].append((e-1,t)) # 시작점에서 끝점으로 가는 도로
    come[e-1].append((s-1,t)) # 시작점에서 끝점으로 오는 도로

# 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력
# => X로 가는 길과 X에서 오는 길의 최소 소요 시간의 합 중에서 최댓값
print(max([d1+d2 for d1,d2 in zip(dijkstra(go),dijkstra(come))]))
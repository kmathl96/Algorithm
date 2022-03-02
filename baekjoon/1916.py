# 최소비용 구하기
# 다익스트라

import sys,heapq
input = sys.stdin.readline

# start에서 end까지 가는 데 걸리는 최소 비용 구하기
def dijkstra(start,end):
    dist = [100000000]*N # 출발점에서 각 도시에 가는 데 걸리는 최소 비용
    dist[start] = 0 # 출발점은 0으로 저장
    q = [(0,start)] # 최소 힙 : (비용, 도시 번호) 저장
    while q:
        w,cur = heapq.heappop(q) # 도시에 가는 데 걸리는 비용, 도시 번호

        # 최소 비용보다 크면 더 갱신할 필요가 없으므로 넘어감
        if dist[cur] < w: continue

        # 갈 수 있는 도시를 탐색하여 비용 갱신
        for node,cost in bus[cur]:
            # 현재 도시를 거쳐서 갈 때 더 적은 비용이 드는 경우
            if w+cost < dist[node]:
                dist[node] = w+cost # 비용 변경
                heapq.heappush(q,(w+cost,node)) # 힙에 넣기
    
    # 도착점까지 가는 데 걸리는 최소 비용 반환
    return dist[end]

N,M = int(input()),int(input()) # 도시의 개수, 버스의 개수

# 버스의 정보 저장
bus = [[] for _ in range(N)]
for _ in range(M):
    start,end,cost = map(int,input().split()) # 출발지와 도착지의 도시 번호, 비용
    bus[start-1].append((end-1,cost))

# A번째 도시에서 B번째 도시까지 가는 데 드는 최소 비용 출력
A,B = map(int,input().split()) # 출발점과 도착점의 도시 번호
print(dijkstra(A-1,B-1)) # 다익스트라를 활용해 최소 비용을 구해서 출력
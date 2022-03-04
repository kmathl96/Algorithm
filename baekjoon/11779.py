# 최소비용 구하기 2
# 다익스트라

import sys,heapq
input = sys.stdin.readline

def dijkstra():
    dist = [[100000000,[start]] for _ in range(n+1)] # 출발지에서 각 도시까지의 거리와 경로
    dist[start][0] = 0
    q = [(0,start)] # 최소 힙
    while q:
        d,cur = heapq.heappop(q) # 거리, 도시 번호
        
        # 마지막 도시에 방문한 경우, 종료
        if cur==end: break
        # 저장된 최단 거리보다 크다면, 더 탐색하고 갱신할 필요가 없음
        if d > dist[cur][0]: continue

        # 연결되어 있는 도시 탐색
        for node,cost in bus[cur]:
            # cur 도시를 방문하는 것이 더 작은 비용이 드는 경우
            if d+cost < dist[node][0]:
                dist[node] = [d+cost,dist[cur][1]+[node]] # 비용과 경로 갱신
                heapq.heappush(q,(d+cost,node)) # 힙에 넣기
    return dist[end]

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

# 버스의 정보 저장
bus = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int,input().split()) # 출발지 번호, 도착지 번호, 비용
    bus[s].append((e,c))

start,end = map(int,input().split()) # 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호
ans = dijkstra()
print(ans[0]) # 출발 도시에서 도착 도시까지 가는데 드는 최소 비용
print(len(ans[1])) # 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수
print(*ans[1]) # 최소 비용을 갖는 경로를 방문하는 도시
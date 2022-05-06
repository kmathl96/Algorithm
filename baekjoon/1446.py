# 지름길
# 다익스트라, DP

### 1. DP ###
N,D = map(int,input().split()) # 지름길의 개수, 고속도로의 길이

# 지름길 정보 저장
roads = [[(i+1,1)] for i in range(D)]
for _ in range(N):
    s,e,d = map(int,input().split()) # 지름길의 시작 위치, 도착 위치, 길이
    if e<=D: roads[s].append((e,d))

dp = list(range(D+1)) # 시작점(0)과의 거리

# 각 위치에서 갈 수 있는 위치를 탐색하며 최단 거리 갱신
for s in range(D):
    for e,d in roads[s]:
        # 시작점에서 s를 거쳐 e로 가는 경로의 거리와 비교하여 최솟값 저장
        dp[e] = min(dp[e],dp[s]+d)
print(dp[D])


### 2. 다익스트라 ###
# import heapq

# N,D = map(int,input().split()) # 지름길의 개수, 고속도로의 길이

# # 지름길 정보 저장
# # 다음 위치와 연결되어 있으므로 다음 위치의 인덱스 값과 거리(1)를 저장
# roads = [[(i+1,1)] for i in range(D+1)]
# roads[D] = [] # 마지막 위치의 지름길 제거
# for _ in range(N):
#     s,e,d = map(int,input().split()) # 지름길의 시작 위치, 도착 위치, 지름길의 길이
    
#     # 도착 위치가 고속도로의 길이 이하인 경우
#     if e<=D:
#         roads[s].append((e,d)) # 지름길 정보 저장

# # 시작점(0)에서 각 위치로 가는 경로의 최단 거리
# dist = [10000]*(D+1)
# dist[0] = 0 # 시작점은 0 저장
# heap = [(0,0)] # 힙에 (거리,위치) 저장
# while heap:
#     d,cur = heapq.heappop(heap) # 시작점과의 거리, 위치 번호
    
#     # 저장된 최단 거리보다 큰 경우, 넘어감
#     if d > dist[cur]: continue

#     # 갈 수 있는 위치와 그 거리
#     for e,l in roads[cur]:
#         # 시작점에서 cur을 거쳐 e로 가는 경로의 거리(d+1)가 더 짧은 경우
#         if dist[e] > d+l:
#             dist[e] = d+l # 거리 갱신
#             heapq.heappush(heap,(d+l,e)) # 힙에 넣기

# # 시작점에서 D 위치까지의 최단 거리 출력
# print(dist[D])
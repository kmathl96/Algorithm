# 배달
# Summer/Winter Coding(~2018)
# 다익스트라

import heapq

def solution(N, road, K):
    INF = float('INF')
    adj = [[INF]*(N+1) for _ in range(N+1)] # 도로를 지날 때 걸리는 시간
    for a,b,c in road:
        # 해당 시간이 더 작은 경우 갱신
        if c < adj[a][b]: adj[a][b],adj[b][a] = c,c
    d = [INF]*(N+1) # 1번 마을에서 각 마을까지 가는 데 걸리는 최소 시간
    d[1] = 0 # 1번 마을이므로 0으로 초기화
    heap = [(0,1)] # 우선순위 큐 : (1번 마을에서 i번 마을까지 걸리는 시간, 마을 번호 i)
    while heap:
        time,cur = heapq.heappop(heap) # 1번 마을~현재 마을 소요 시간, 현재 마을 번호
        if d[cur] < time: continue
        for i in range(1,N+1):
            new_time = time+adj[cur][i] # 1번 마을~현재 마을 소요 시간 + 현재 마을~i번 마을 소요 시간
            if d[i] > new_time: # 1번 마을~i번 마을 소요 시간보다 작은 경우 갱신
                d[i] = new_time
                heapq.heappush(heap, (new_time,i))
    return sum([1 if t<=K else 0 for t in d]) # 음식 배달 가능 시간이 K 이하인 마을의 개수

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4
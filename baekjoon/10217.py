# KCM Travel
# 다익스트라, DP

import sys,heapq
input = sys.stdin.readline

def dijkstra(N,M,graph):
    # dist[city][cost] = time
    # => 1번 도시(인천)에서 각 도시에 도착하며 cost 이하의 비용을 쓰는 경로의 최단 시간
    dist = [[100000]*(M+1) for _ in range(N+1)]
    
    q = [(0,0,1)] # 최소 힙
    dist[1][0] = 0
    
    while q:
        d,c,cur = heapq.heappop(q) # 시간, 비용, 현재 도시

        # 마지막 도시(LA)인 경우 종료
        if cur==N and c==M: break
        # 저장된 최단 시간보다 큰 경우, 더 갱신하지 않고 넘어감
        if dist[cur][c] < d: continue

        # 현재 도시와 연결된 도시 탐색
        for node,cost,time in graph[cur]: # 도시 번호, 가는 데 걸리는 비용과 시간
            # 현재 도시를 거쳐 해당 도시를 가는 데 걸리는 비용과 시간
            nc,nt = c+cost,d+time

            # 비용이 M 이하이고 저장된 최단 시간보다 작은 경우, 갱신
            if nc <= M and nt < dist[node][nc]:
                # 비용이 M 이하인 모든 경우의 최단 시간 갱신
                for new_c in range(nc,M+1):
                    # 해당 비용의 최단 시간보다 크다면 종료
                    if dist[node][new_c] <= nt: break
                    dist[node][new_c] = nt # 최단 시간 갱신
                heapq.heappush(q,(nt,nc,node)) # 더 탐색하고 갱신하기 위해 힙에 넣기
    
    return dist[N][M] # N번 도시(LA)로 가는 데 M 이하의 비용이 걸리는 경우의 최단 시간

def sol():
    T = int(input()) # 테스트 케이스의 수
    answer = [] # 각 테스트 케이스의 결과를 넣을 리스트

    for _ in range(T):
        N,M,K = map(int,input().split()) # 공항의 수, 총 지원비용, 티켓정보의 수
        # 티켓정보 저장하기
        graph = [[] for _ in range(N+1)]
        for _ in range(K):
            u,v,c,d = map(int,input().split()) # 각 티켓의 출발공항, 도착공항, 비용, 소요시간
            graph[u].append((v,c,d))
        
        # 찬민이 LA에 도착하는 데 걸리는 가장 짧은 소요시간 구하기
        # LA에 도착할 수 없는 경우 "Poor KCM"을 출력
        ans = dijkstra(N,M,graph)
        answer.append(ans if ans<100000 else 'Poor KCM')
    
    # 각 테스트 케이스의 결과를 한 줄에 하나씩 출력
    for ans in answer: print(ans)

sol()
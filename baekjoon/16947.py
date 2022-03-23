# 서울 지하철 2호선

import sys
input = sys.stdin.readline

def sol():
    N = int(input()) # 역의 개수
    adj = [[0]*N for _ in range(N)] # 인접 행렬
    edges = [0]*N # 각 역이랑 연결된 간선의 개수
    for _ in range(N):
        v1,v2 = map(int,input().split()) # 두 역의 번호
        adj[v1-1][v2-1],adj[v2-1][v1-1] = 1,1 # 인접 표시
        
        # 간선 개수 증가
        edges[v1-1] += 1
        edges[v2-1] += 1
    
    parents = [-1]*N # 부모 노드(역)의 번호

    # 순환선에 포함되지 않는 역 찾기
    not_cycle = [v for v in range(N) if edges[v]==1] # 1개인 역은 순환선이 아님
    while not_cycle:
        v1 = not_cycle.pop() # 현재 역 번호
        
        # 인접한 역 탐색
        for v2 in range(N):
            if not adj[v1][v2]: continue # 연결되어 있지 않으면 넘어감
            adj[v1][v2],adj[v2][v1] = 0,0 # 간선 정보를 지움 (중복 방문 방지)
            
            # 간선 개수 감소
            edges[v1] -= 1
            edges[v2] -= 1
            
            parents[v1] = v2 # v1의 부모를 v2로 저장
            
            # v2의 간선이 1개인 경우, v2도 순환선이 아님
            if edges[v2]==1:
                not_cycle.append(v2)
    
    # 순환선과의 거리 구하기
    dist = [0]*N
    for v in range(N):
        cnt = 0 # 거리
        p = parents[v] # 부모

        # 부모가 존재하지 않을 때까지(= 순환선인 역을 만날 때까지) 반복
        while p!=-1:
            p = parents[p]
            cnt += 1 # 거리 증가
        dist[v] = cnt # 거리 저장
    
    # 각 역과 순환선 사이의 거리를 공백으로 구분해 출력
    print(*dist)

sol()
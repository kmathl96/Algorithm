# 서강그라운드
# 플로이드-와샬

def sol():
    n,m,r = map(int,input().split()) # 지역의 개수, 수색범위, 길의 개수
    items = list(map(int,input().split())) # 각 지역에 있는 아이템의 수
    dist = [[0]*(n+1) for _ in range(n+1)] # 지역 간 거리
    for _ in range(r):
        a,b,l = map(int,input().split()) # 길 양 끝에 존재하는 지역의 번호, 길의 길
        dist[a][b],dist[b][a] = l,l # 거리 저장
    
    # 지역 간 최단 거리 구하기
    for k in range(1,n+1):
        for r in range(1,n+1):
            # r-k가 연결되어 있지 않다면 넘어감
            if not dist[r][k]: continue
            for c in range(1,n+1):
                # 본인 지역이거나, k-c가 연결되어 있지 않다면 넘어감
                if r==c or not dist[k][c]: continue

                # 아직 r-c가 연결되어 있지 않거나, r-k-c 경로의 거리보다 긴 경우
                if not dist[r][c] or dist[r][c] > dist[r][k] + dist[k][c]:
                    dist[r][c] = dist[r][k] + dist[k][c] # 거리 갱신
    
    # 예은이가 얻을 수 있는 아이템의 최대 개수 구하기
    ans = 0
    # r번 지역에 떨어지는 경우 얻을 수 있는 아이템의 최대 개수 구하기
    for r in range(1,n+1):
        cnt = items[r-1] # 떨어지는 지역의 아이템의 수 저장
        for c in range(1,n+1):
            # 갈 수 있는 지역인 경우
            if 0 < dist[r][c] <= m:
                cnt += items[c-1] # 해당 지역의 아이템의 수 더하기
        
        # 개수가 더 많다면 저장
        if ans < cnt: ans = cnt
    
    print(ans)

sol()
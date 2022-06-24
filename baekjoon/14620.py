# 꽃길
# 브루트포스, DFS

def dfs(v,cost,cnt,row,col):
    global ans

    # 씨앗 3개를 다 심었을 때 탐색 종료
    if cnt==3:
        # 비용이 ans보다 작다면 갱신
        if ans > cost:
            ans = cost
        return

    # (row,col) 이후의 칸들을 탐색
    for r in range(row,N-1):
        for c in range(1,N-1):
            # 이전 칸이거나 꽃이 피는 자리인 경우, 탐색하지 않고 넘어감
            if (r==row and c<=col or v[r][c]): continue

            tmp = G[r][c] # 해당 씨앗에서 피는 꽃이 차지하는 화단 대여 비용
            flag = 1 # 꽃이 필 수 있는지 여부

            # 꽃이 피는 자리 탐색
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i] # 탐색할 자리
                # 이미 꽃이 피는 땅인 경우, 탐색 종료
                if v[nr][nc]:
                    flag = 0
                    break
                tmp += G[nr][nc] # 해당 땅의 가격만큼 비용 증가
            
            # 꽃이 필 수 없는 경우, 더 탐색하지 않고 넘어감
            if not flag: continue

            # 꽃이 피는 땅 체크
            v[r][c] = 1 # 씨앗 심는 땅
            for i in range(4):
                v[r+dr[i]][c+dc[i]] = 1 # 꽃잎이 피는 땅
            # 탐색
            dfs(v,cost+tmp,cnt+1,r,c)
            # 방문 체크 해제
            v[r][c] = 0
            for i in range(4):
                v[r+dr[i]][c+dc[i]] = 0

N = int(input()) # 화단의 한 변의 길이
G = [list(map(int,input().split())) for _ in range(N)] # 화단의 지점당 가격
visited = [[0]*N for _ in range(N)] # 방문 배열
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 벡터
ans = 3000 # 꽃을 심기 위한 최소 비용
dfs(visited,0,0,1,0) # 탐색하면서 최소 비용 갱신
print(ans)
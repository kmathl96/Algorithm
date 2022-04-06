# 빙산
# 구현, DFS

import sys
input = sys.stdin.readline

def dfs(row,col):
    st = [(row,col)] # 스택
    removed = [] # 녹는 빙산

    # 탐색
    while st:
        r,c = st.pop() # 현재 칸의 위치 좌표
        cnt0 = 0 # 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수
        
        # 사방 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치
            
            # 0인 경우, 0의 개수 증가
            if not arr[nr][nc]:
                cnt0 += 1
            
            # 0이 아닌 경우, 아직 탐색하지 않은 곳이라면 더 탐색하기
            elif not visited[nr][nc]:
                visited[nr][nc] = 1
                st.append((nr,nc)) # 스택에 넣기

        # 해당 칸의 위치와 그 빙산이 녹는 높이 정보 저장
        removed.append((r,c,cnt0))
    
    # 빙하 녹기
    for r,c,cnt0 in removed:
        arr[r][c] -= cnt0
        
        # 최소 높이는 0
        if arr[r][c]<0:
            arr[r][c] = 0

N,M = map(int,input().split()) # 배열의 크기
arr = [list(map(int,input().split())) for _ in range(N)] # 각 칸의 빙산의 높이
t = 0 # 시간
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
while True:
    cnt = 0 # 빙산의 개수
    visited = [[0]*M for _ in range(N)] # 방문 배열
    for r in range(1,N-1):
        for c in range(1,M-1):
            # 빙산이 있는 위치이며 아직 방문하지 않은 경우 DFS로 탐색
            if arr[r][c] and not visited[r][c]:
                cnt += 1 # 빙산의 개수 증가
                visited[r][c] = 1 # 방문 표시
                dfs(r,c)
    
    # 빙산이 다 녹거나 2개 이상인 경우(=분리됨) 경우, 종료
    if cnt!=1: break

    # 시간 증가
    t += 1

# 빙하가 있는 경우, 분리될 때까지 걸린 시간 출력
# 분리되지 않고 다 녹은 경우, 0 출력
print(t if cnt else 0)
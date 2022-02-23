# 다리 만들기
# BFS

from collections import deque

dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향
def bfs(row,col):
    global ans, board

    q = deque([(row,col,0)]) # 큐
    visited = [[0]*N for _ in range(N)] # 방문 배열
    visited[row][col] = 1 # 방문 체크

    # 1. 섬 덩어리 찾기
    st = [(row,col)]
    board[row][col] = 0
    while st:
        r,c = st.pop()
        
        # 사방 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치
            # 유효한 위치이며 섬인 경우
            if 0<=nr<N and 0<=nc<N and board[nr][nc]:
                board[nr][nc] = 0 # 더 탐색하지 않도록 0으로 변경
                st.append((nr,nc)) # 섬을 더 찾기 위해 스택에 넣기
                q.append((nr,nc,0)) # 이따가 다른 섬을 찾기 위해 큐에 넣기
    
    # 2. 다른 섬과의 가장 짧은 거리 구하기
    while q:
        r,c,d = q.popleft() # 위치와 거리
        
        # 섬이라면 더 탐색하지 않고 종료
        if board[r][c]:
            ans = min(ans,d-1) # 정답 갱신
            return
        
        # 사방 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치
            # 유효한 위치이면서 아직 방문하지 않은 곳인 경우
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                q.append((nr,nc,d+1)) # 큐에 넣기
                visited[nr][nc] = 1 # 방문 표시

N = int(input()) # 지도의 크기
board = [list(map(int,input().split())) for _ in range(N)] # 지도의 상태

# 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법 찾기
ans = N*N # 가장 짧은 다리의 길이
for r in range(N):
    for c in range(N):
        # 섬일 때 같은 섬 덩어리를 찾고,
        # 다른 섬과의 가장 가까운 거리를 구해서 ans 갱신
        if board[r][c]: bfs(r,c)
print(ans)
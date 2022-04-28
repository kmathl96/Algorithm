# 로봇
# BFS

from collections import deque

M,N = map(int,input().split()) # 직사각형의 세로 길이와 가로 길이
board = [list(map(int,input().split())) for _ in range(M)] # 궤도 설치 상태
sr,sc,sd = map(int,input().split()) # 로봇의 출발 지점의 위치와 바라보는 방향
er,ec,ed = map(int,input().split()) # 로봇의 도착 지점의 위치와 바라보는 방향
dr,dc = [0,0,0,1,-1],[0,1,-1,0,0] # 방향 배열
q = deque([(sr-1,sc-1,sd,0)]) # 큐 : 현재 위치와 방향, 이동 횟수를 담음

# 방문 배열
# visisted[r][c][d] : (r,c)의 위치에 d 방향으로 방문했는지 체크
visited = [[[0]*5 for _ in range(N)] for _ in range(M)]
visited[sr-1][sc-1][sd] = 1 # 출발 지점 방문 체크
while q:
    r,c,d,cnt = q.popleft() # 현재 위치와 방향, 이동 횟수

    # 도착 지점에 원하는 방향으로 도달한 경우, 종료
    if r==er-1 and c==ec-1 and d==ed: break

    # 명령 1. Go k
    # 현재 향하고 있는 방향으로 1~3칸 만큼 움직임
    for i in range(1,4):
        nr,nc = r+dr[d]*i,c+dc[d]*i # 이동할 위치
        
        # 유효한 위치가 아니거나 궤도가 없어 갈 수 없는 경우, 더 갈 수 없으므로 종료
        if not (0<=nr<M and 0<=nc<N) or board[nr][nc]: break

        # 이미 방문한 경우, 넘어감
        if visited[nr][nc][d]: continue

        visited[nr][nc][d] = 1 # 방문 체크
        q.append((nr,nc,d,cnt+1)) # 큐에 넣기
    
    # 명령 2. Turn dir
    # 왼쪽/오른쪽으로 90도 회전함
    for i in range(1,4):
        nd = (d+i-1)%4+1 # 새로운 방향
        
        # 왼쪽/오른쪽으로 90도 회전하는 방향이며, 아직 방문한 적 없는 경우
        if (d+nd)%4 != 3 and not visited[r][c][nd]:
            visited[r][c][nd] = 1 # 방문 체크
            q.append((r,c,nd,cnt+1)) # 큐에 넣기

print(cnt)
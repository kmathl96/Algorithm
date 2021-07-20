# 연구소 3
# BFS, 브루트포스

from itertools import combinations
from collections import deque

N,M = map(int,input().split()) # 연구소의 크기, 놓을 수 있는 바이러스의 개수
board = [list(map(int,input().split())) for _ in range(N)] # 연구소의 상태
virus = [] # 바이러스를 담을 리스트
empty = 0 # 빈 칸의 개수
for r in range(N):
    for c in range(N):
        if board[r][c] == 2: virus.append((r,c,0)) # 바이러스의 좌표와 거리
        elif board[r][c] == 0: empty += 1 # 빈 칸 개수 증가

dr,dc = [-1,0,1,0],[0,1,0,-1]
ans = 2500 # 모든 빈 칸에 바이러스가 있게 되는 최소 시간
for case in combinations(virus, M): # M개의 바이러스 조합
    q = deque(case) # 바이러스를 넣음
    visited = [[0]*N for _ in range(N)] # 방문 리스트
    for r,c,d in case:
        visited[r][c] = 1 # 바이러스가 있는 칸은 체크
    cnt,last = 0,0 # 바이러스로 바뀐 빈 칸의 개수, 마지막으로 바이러스가 번진 칸과의 거리
    while q:
        r,c,d = q.popleft() # 좌표와 거리

        # 거리가 ans보다 커지면 더 탐색할 필요가 없으므로 종료
        # 빈 칸이 모두 바이러스로 바뀐 경우 종료
        if ans <= d or cnt==empty: break

        for i in range(4): # 상하좌우로 인접한 칸 탐색
            nr,nc = r+dr[i],c+dc[i]
            # 유효한 좌표이고, 아직 방문하지 않았으며 벽이 아닌 경우, 더 탐색함
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and board[nr][nc]!=1:
                q.append((nr,nc,d+1)) # 더 탐색하기 위해 좌표와 그 거리를 큐에 넣음
                visited[nr][nc] = 1 # 방문 체크
                if not board[nr][nc]: # 빈 칸인 경우
                    cnt += 1 # 바이러스로 변한 빈 칸의 개수 증가
                    last = d+1 # 바이러스가 번진 칸과의 거리 갱신
    
    # 모든 빈 칸이 바이러스로 바뀌었고, 그 시간이 ans보다 작으면 ans 변경
    if cnt == empty and ans > last: ans = last

print(ans if ans<2500 else -1) # ans 값이 초기값 그대로이면 -1, 아니면 그 값 출력
# 토마토
# 그래프와 BFS

from collections import deque

M,N = map(int, input().split())
box = [list(map(int,input().split())) for _ in range(N)]
# 익은 토마토가 들어있는 상자의 위치를 q에 넣음
q = deque()
for r in range(N):
    for c in range(M):
        if box[r][c]==1: q.append((r,c,0))
dr,dc = [-1,0,1,0],[0,1,0,-1]
while q:
    r,c,d = q.popleft() # 해당 토마토의 위치와 익는 데 걸린 일수
    for i in range(4): # 사방 탐색
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M and not box[nr][nc]:
            box[nr][nc] = 1
            q.append((nr,nc,d+1))
for row in box:
    if 0 in row: # 하나라도 0 존재 = 토마토가 다 익지 않음
        d = -1 # -1을 출력하기 위함
        break
print(d)
# 미로 탐색
# 그래프와 BFS

from collections import deque

N,M = map(int,input().split())
maze = [list(input()) for _ in range(N)]
q = deque([(0,0,1)]) # 시작점의 위치와 지나온 칸 수(1)을 넣음
dr,dc = [-1,0,1,0],[0,1,0,-1]
while q:
    r,c,d = q.popleft()
    if r==N-1 and c==M-1: break # 도착했을 경우 끝냄
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M and maze[nr][nc]=='1':
            q.append((nr,nc,d+1))
            maze[nr][nc] = '0' # 지나온 길은 다시 가지 않도록 값을 바꿔줌
print(d)
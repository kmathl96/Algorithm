# 알고스팟
# 그래프와 BFS
# 가장 벽을 적게 부실 수 있는 경우를 빨리 찾기 위해
# 벽이 없는 경우 q의 앞에 삽입, 벽이 있는 경우 q의 뒤에 삽입하여
# 적게 부신 경우를 먼저 탐색하도록 함

from collections import deque

M,N = map(int,input().split())
arr = [list(input()) for _ in range(N)]
dist = [[200]*M for _ in range(N)] # N,M의 입력값이 100이하이므로 최대 횟수가 200
dist[0][0] = 0 # 벽 부신 횟수
q = deque([(0,0)])
dr,dc = [-1,0,1,0],[0,1,0,-1]
while q:
    r,c = q.popleft()
    if r==N-1 and c==M-1: break # 도착점에 도달한 경우 그 최소값을 찾은 것
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M:
            if dist[nr][nc]!=200: continue # 이미 벽 부신 횟수가 저장돼 있는 경우 = 그것이 최소 횟수이므로 통과
            if arr[nr][nc]=='1':
                dist[nr][nc] = dist[r][c]+1 # 벽이 있으므로 현재 횟수+1 저장
                q.append((nr,nc)) # 뒤에 삽입
            else:
                dist[nr][nc] = dist[r][c]
                q.appendleft((nr,nc)) # 앞에 삽입하여 먼저 탐색
print(dist[N-1][M-1])
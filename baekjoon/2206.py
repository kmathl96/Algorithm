# 벽 부수고 이동하기
# 그래프와 BFS
# 벽 부쉈는지 여부에 따라 경로 거리가 달라지므로 visited를 3차원으로 만들어야 함
# visited[row][col][벽 부쉈는지 여부] = 시작점부터 해당 위치까지의 최단 거리

from collections import deque

N,M = map(int,input().split())
mp = [list(input()) for _ in range(N)]
visited = [[[0]*2 for i in range(M)] for j in range(N)]
visited[0][0][0] = 1 # 시작점도 포함
ans = -1 # ans 값이 바뀌지 않았을 경우(=경로 찾기 불가능) -1 출력
q = deque([(0,0,0)]) # 위치와 벽 부쉈는지 여부
dr,dc = [-1,0,1,0],[0,1,0,-1]
while q:
    r,c,broke = q.popleft()
    if r==N-1 and c==M-1:
        ans = visited[N-1][M-1][broke]
        break
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc][broke]:
            if mp[nr][nc]=='0':
                visited[nr][nc][broke] = visited[r][c][broke]+1
                q.append((nr,nc,broke))
            elif mp[nr][nc]=='1' and not broke:
                visited[nr][nc][1] = visited[r][c][broke]+1
                q.append((nr,nc,1)) # 벽을 부쉈으므로 1로 넣음
print(ans)
# 섬의 개수
# 그래프와 BFS

from collections import deque

dr,dc = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
def bfs(row,col):
    global map_
    q = deque([(row,col)])
    while q:
        r,c = q.popleft()
        for i in range(8): # 팔방 탐색
            nr,nc = r+dr[i],c+dc[i]
            # 탐색하는 곳이 지도 내에 있으며 섬인 경우, 그 위치에서도 탐색
            if 0<=nr<h and 0<=nc<w and map_[nr][nc]:
                q.append((nr,nc))
                map_[nr][nc] = 0 # 나중에 또 탐색하지 않도록 0으로 값 바꿈

while True:
    w,h = map(int,input().split())
    if w==0 and h==0: break
    map_ = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0 # 섬의 개수
    for r in range(h):
        for c in range(w):
            if map_[r][c]:
                bfs(r,c)
                cnt += 1
    print(cnt)
    
            
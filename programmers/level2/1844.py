# 게임 맵 최단거리
# 찾아라 프로그래밍 마에스터
# BFS

from collections import deque

dr,dc = [-1,0,1,0],[0,1,0,-1]

def solution(maps):
    n,m = len(maps),len(maps[0]) # 맵의 세로 길이, 맵의 가로 길이
    q = deque([(0,0,1)]) # 내 캐릭터의 처음 위치와 현재 위치한 칸 1칸
    while q:
        r,c,cnt = q.popleft() # 현재 위치와 지나온 칸 수
        if r==n-1 and c==m-1: return cnt # 상대 팀 진영에 도착하면 지나온 칸 수 반환
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 이동하려는 위치
            if 0<=nr<n and 0<=nc<m and maps[nr][nc]: # 해당 위치가 유효한 경우(맵 내에 있으며 벽이 없음)
                q.append((nr,nc,cnt+1)) # 이동한 위치와 지나온 칸수+1 넣기
                maps[nr][nc] = 0 # 지나온 위치는 다시 방문하지 않도록 0으로 처리
    return -1 # 상대 팀 진영에 도착하지 못하면 -1 반환

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1
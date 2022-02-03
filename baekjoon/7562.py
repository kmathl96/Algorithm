# 나이트의 이동
# BFS

from collections import deque
import sys
input = sys.stdin.readline

# BFS 함수
# (함수로 구현하는 것이 실행속도가 훨씬 빠름)
def bfs():
    visited = [[0]*l for _ in range(l)] # 방문 여부
    q = deque([(x,y,0)]) # 큐 : 나이트의 처음 위치와 이동 횟수 0을 넣기
    visited[x][y] = 1 # 처음 위치 방문 체크
    
    # 이동할 수 있는 모든 칸 탐색
    while q:
        r,c,d = q.popleft() # 현재 위치의 좌표와 이동한 횟수

        # 현재 위치가 목적지의 좌표와 같다면 이동 횟수 반환하고 종료
        if r==dest_x and c==dest_y: return d

        # 나이트가 이동할 수 있는 여덟 칸 탐색
        for i in range(8):
            nr,nc = r+dr[i],c+dc[i] # 이동할 칸

            # 유효한 위치이며 아직 방문하지 않은 칸인 경우
            if 0<=nr<l and 0<=nc<l and not visited[nr][nc]:
                q.append((nr,nc,d+1)) # 탐색하기 위해 큐에 넣음
                visited[nr][nc] = 1 # 방문 체크

dr,dc = [-1,-2,-2,-1,1,2,2,1],[-2,-1,1,2,2,1,-1,-2] # 나이트가 이동할 수 있는 방향
for _ in range(int(input())):
    l = int(input()) # 체스판의 한 변의 길이
    x,y = map(int,input().split()) # 나이트가 현재 있는 칸
    dest_x,dest_y = map(int,input().split()) # 나이트가 이동하려고 하는 칸
    print(bfs()) # BFS의 결과를 출력
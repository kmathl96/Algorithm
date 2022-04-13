# 말이 되고픈 원숭이
# BFS

from collections import deque
import sys
input = sys.stdin.readline

def sol():
    K = int(input()) # 말처럼 움직일 수 있는 횟수
    W,H = map(int,input().split()) # 격자판의 가로 길이와 세로 길이
    board = [list(map(int,input().split())) for _ in range(H)] # 격자판
    dr,dc = [[-1,0,1,0],[-1,-2,-2,-1,1,2,2,1]],[[0,1,0,-1],[-2,-1,1,2,2,1,-1,-2]] # 방향 배열 (원숭이의 이동방향, 말의 이동방향)
    q = deque([(0,0,0,0)]) # 큐
    visited = [[[0]*W for _ in range(H)] for _ in range(K+1)]
    while q:
        r,c,d,cnt = q.popleft() # 원숭이의 위치 좌표, 동작 수, 말처럼 움직인 횟수
        
        # 도착점에 도착한 경우, BFS 종료
        if r==H-1 and c==W-1:
            return d # 동작 수 반환
        
        # 탐색
        # 1. 인접한 네 방향으로 움직임
        # 2. 말의 움직임으로 움직임
        for j in range(2):
            for i in range(len(dr[j])):
                nr,nc = r+dr[j][i],c+dc[j][i] # 이동할 위치

                # 유효한 위치이며, 평지이고, 현재 말의 움직임의 횟수로는 아직 방문하지 않은 곳인 경우
                if 0<=nr<H and 0<=nc<W and not board[nr][nc] and not visited[cnt+j][nr][nc]:
                    visited[cnt+j][nr][nc] = 1 # 방문 표시
                    q.append((nr,nc,d+1,cnt+j)) # 더 탐색하기 위해 큐에 넣기
            
            # 말처럼 움직인 횟수가 K와 같으면 말의 움직임으로 이동할 수 없으므로 종료
            if cnt == K: break
    
    # 도착점에 도달하지 못한 경우, -1 반환
    return -1

print(sol())
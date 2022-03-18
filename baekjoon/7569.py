# 토마토
# BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs(tomato,q,cnt,M,N,H):
    dx,dy,dz = [0,0,0,0,-1,1],[0,0,-1,1,0,0],[-1,1,0,0,0,0] # 방향 배열
    while q:
        x,y,z,d = q.popleft() # 현재 토마토의 좌표와 익는 데 걸리는 시간
        # 인접한 칸 탐색
        for i in range(6):
            nx,ny,nz = x+dx[i],y+dy[i],z+dz[i] # 탐색할 칸
            # 유효한 위치이며 토마토가 아직 익지 않은 경우
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and not tomato[nz][nx][ny]:
                tomato[nz][nx][ny] = 1 # 익었다고 표시
                cnt -= 1 # 익지 않은 토마토의 개수 감소
                q.append((nx,ny,nz,d+1)) # 큐에 넣기
    
    # 모두 익는 데 걸린 시간 출력
    # 익지 않은 토마토가 있는 경우, -1 출력
    return -1 if cnt else d

def sol():
    M,N,H = map(int,input().split()) # 상자의 크기와 쌓아올려지는 상자의 수
    tomato = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)] # 토마토들의 정보
    q = deque() # 큐
    cnt = 0 # 익지 않은 토마토의 개수
    for z in range(H):
        for x in range(N):
            for y in range(M):
                # 익은 토마토는 큐에 좌표 넣기
                if tomato[z][x][y]==1: q.append((x,y,z,0))
                # 익지 않은 토마토 개수 세기
                elif not tomato[z][x][y]: cnt += 1
    
    # 토마토가 모두 익을 때까지 최소 며칠이 걸리는지 구하기
    print(bfs(tomato,q,cnt,M,N,H))

sol()
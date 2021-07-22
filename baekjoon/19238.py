# 스타트 택시
# 구현, BFS, 시뮬레이션

from collections import deque

N,M,fuel = map(int,input().split()) # 활동할 영역의 크기, 승객 수, 초기 연료의 양
board = [list(map(int,input().split())) for _ in range(N)] # 활동할 영역의 지도
pos = list(map(lambda x: int(x)-1,input().split())) # 백준의 현재 위치

# 각 칸에 있는 승객의 목적지
passengers = [[0]*N for _ in range(N)]
for _ in range(M):
    sr,sc,er,ec = map(int,input().split()) # 승객의 출발지와 목적지의 좌표
    passengers[sr-1][sc-1] = (er-1,ec-1) # 목적지 좌표 넣기

dr,dc = [-1,0,1,0],[0,1,0,-1]

# M명의 손님 이동시키기
for _ in range(M):
    # 태울 승객 찾기
    q1 = deque([(pos[0],pos[1],0)]) # 좌표와 거리
    dist = 400 # 태울 승객과의 거리
    pr,pc = N,N # 태울 승객의 좌표
    visited = [[0]*N for _ in range(N)]
    visited[pos[0]][pos[1]] = 1
    while q1:
        r,c,d = q1.popleft()
        if d > dist: break # 태울 승객과의 거리보다 크면 더 탐색할 필요가 없으므로 종료
        
        # 해당 칸에 승객이 있으며,
        # 행 번호가 더 작거나, 같은 행이라면 열 번호가 더 작은 경우
        if passengers[r][c] and (r<pr or (r==pr and c<pc)):
            pr,pc = r,c # 태울 승객 좌표 갱신
            dist = d # 승객과의 거리 갱신
        
        # 인접한 칸 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            # 유효한 위치이고, 빈 칸이며, 아직 방문하지 않은 칸인 경우
            if 0<=nr<N and 0<=nc<N and not board[nr][nc] and not visited[nr][nc]:
                q1.append((nr,nc,d+1)) # 큐에 넣기
                visited[nr][nc] = 1
    
    # 거리가 연료 양보다 크거나 태울 승객을 못 찾은 경우, 업무 종료
    if dist > fuel or pr==N:
        fuel = -1 # -1로 변경
        break
    
    # 승객의 위치까지 이동
    fuel -= dist # 거리 만큼 연료 양 감소

    # 승객의 목적지까지의 최단 거리 찾기
    q2 = deque([(pr,pc,0)]) # 좌표와 거리
    visited = [[0]*N for _ in range(N)]
    visited[pr][pc] = 1
    while q2:
        r,c,d = q2.popleft()
        if (r,c)==passengers[pr][pc]: break # 해당 좌표가 목적지인 경우, 종료
        
        # 인접한 칸 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            # 유효한 위치이고, 빈 칸이며, 아직 방문하지 않은 칸인 경우
            if 0<=nr<N and 0<=nc<N and not board[r][c] and not visited[nr][nc]:
                q2.append((nr,nc,d+1))
                visited[nr][nc] = 1

    # 거리가 연료 양보다 크거나 승객의 목적지까지 가지 못하는 경우, 종료
    if d > fuel or (r,c)!=passengers[pr][pc]:
        fuel = -1 # -1로 변경
        break

    # 승객을 목적지로 이동
    fuel += d # 연료 양 충전 (d만큼 소모, d*2만큼 충전 => d만큼 더하기)
    pos = passengers[pr][pc] # 백준의 위치 갱신
    passengers[pr][pc] = 0 # 승객의 목적지 정보 제거
print(fuel) # 남은 연료의 양 (이동하지 못한 경우 -1) 출력
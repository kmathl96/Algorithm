# 아기 상어
# 구현, BFS, 시뮬레이션

from collections import deque

dr,dc = [-1,0,0,1],[0,-1,1,0]
N = int(input()) # 공간의 크기
arr = [list(map(int,input().split())) for _ in range(N)] # 공간의 상태

# 아기 상어의 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            sr,sc,size = i,j,2 # 아기 상어의 위치와 크기
            break

# 아기 상어가 혼자 물고기를 잡아먹을 수 있는 시간, 현재 크기에서 먹은 물고기 수
time,eat_cnt = 0,0

while True:
    arr[sr][sc] = 0 # 상어의 위치를 0으로 변경
    q = deque([(sr,sc,0)]) # 상어가 지나갈 칸
    visited = [[0]*N for _ in range(N)] # 방문 여부
    visited[sr][sc] = 1 # 현재 위치 체크

    # 먹을 물고기와의 거리
    # N의 최대 크기(20)를 이용해 충분히 큰 수로 초기화함
    # (처음에 대각선 양 끝 지점의 최소 거리(20*2 정도)로 초기화해서 실패..
    # 지그재그로 가는 경우를 생각해보면,
    # 대각선 양 끝 지점의 최대 거리(20**2 정도)로 초기화해야 함)
    dist = 400

    eat = [] # 먹을 물고기의 좌표와 거리를 담을 리스트
    while q:
        r,c,d = q.popleft()
        if d > dist: break # 먹을 물고기와의 거리보다 멀면 더 탐색할 필요가 없으므로 종료
        for i in range(4): # 사방으로 인접한 칸 탐색
            nr,nc = r+dr[i],c+dc[i] # 탐색할 좌표
            # 유효한 위치이며, 아직 지나가지 않았고, 상어의 크기보다 작거나 같은 경우만 탐색
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and arr[nr][nc]<=size:
                visited[nr][nc] = 1 # 방문 체크
                q.append((nr,nc,d+1)) # 지나갈 위치와 그 거리

                # 먹을 수 있는 물고기인 경우
                if 0<arr[nr][nc]<size:
                    dist = d # 그 거리 저장

                    # 먹을 물고기가 아직 저장되지 않은 상태이거나(먹을 수 있는 첫 물고기),
                    # 먹을 물고기보다 행 위치가 작거나(= 위에 있음),
                    # 먹을 물고기와 행 위치가 같고 열 위치는 작은(= 왼쪽에 있음) 경우
                    if not eat or nr < eat[0] or (nr==eat[0] and nc<eat[1]):
                        eat = [nr,nc,d+1] # 먹을 물고기의 위치와 거리 갱신
    
    # 먹을 물고기가 없다면 종료
    if not eat: break

    # 물고기를 먹음
    sr,sc,d = eat # 상어 위치 갱신
    time += d # 거리 만큼 시간이 지남
    eat_cnt += 1 # 크기 1 증가

    # 상어는 자신의 크기과 같은 수의 물고기를 먹을 때마다 크기 1 증가
    if eat_cnt == size:
        eat_cnt = 0 # 먹은 물고기 수 초기화
        size += 1 # 크기 증가
print(time) # 물고기를 잡아먹은 시간 출력
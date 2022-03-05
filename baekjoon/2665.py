# 미로만들기
# 다익스트라

import sys,heapq
input = sys.stdin.readline

n = int(input()) # 한 줄에 들어가는 방의 수
room = [input() for _ in range(n)] # 방의 상태
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향배열

# 다익스트라
# (0,0)에서 각 방까지 가는 데 흰 방으로 바꾸어야 할 최소의 검은 방의 수
dist = [[1000]*n for _ in range(n)]
dist[0][0] = 0 # 시작방은 항상 흰 방이므로 0
q = [(0,0,0)] # 최소 힙 : (바꿔야 할 방의 개수, 행 인덱스, 열 인덱스)
while q:
    d,r,c = heapq.heappop(q)

    # 끝방에 도착했다면 종료
    if r==n-1 and c==n-1: break
    # 저장된 최솟값보다 크다면 더 탐색할 필요가 없으므로 넘어감
    if d > dist[r][c]: continue

    # 인접한 칸 탐색
    for i in range(4):
        nr,nc,nd = r+dr[i],c+dc[i],d # 탐색할 칸의 위치와 바꿀 방의 수
        if 0<=nr<n and 0<=nc<n:
            # 탐색할 방이 검은 방인 경우, 흰 방으로 바꿔야 함
            if room[nr][nc]=='0':
                nd += 1 # 바꿔야 할 방의 수 증가
            
            # 저장된 값보다 작다면 갱신
            if dist[nr][nc] > nd:
                dist[nr][nc] = nd
                heapq.heappush(q,(nd,nr,nc)) # 힙에 넣기

# 끝방까지 가는 데 검은 방에서 흰 방으로 바꾸어야 할 최소의 수 출력
print(dist[n-1][n-1])
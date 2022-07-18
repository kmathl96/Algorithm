# 데스 나이트
# BFS

from collections import deque

N = int(input()) # 체스판의 크기

# 데스 나이트의 시작점(r1,c1)과 도착점(r2,c2)
r1,c1,r2,c2 = map(int,input().split())
q = deque([(r1,c1,0)]) # 큐

# 데스 나이트가 시작점에서 도착점으로 이동하는 최소 이동 횟수 구하기
ans = -1 # 이동할 수 없는 경우에는 -1을 출력해야 하므로 -1로 초기화

dr,dc = [-2,-2,0,0,2,2],[-1,1,-2,2,-1,1] # 방향 배열
visited = [[0]*N for _ in range(N)] # 방문 배열
visited[r1][c1] = 1 # 시작점 방문 체크
while q:
    r,c,d = q.popleft() # 현재 위치와 이동 횟수

    # 도착점과 일치하는 경우, 이동 횟수를 저장하고 탐색 종료
    if r==r2 and c==c2:
        ans = d
        break

    # 이동할 수 있는 칸 탐색
    for i in range(6):
        nr,nc = r+dr[i],c+dc[i] # 이동할 위치
        # 유효한 위치이며 아직 방문하지 않은 경우, 이동
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            visited[nr][nc] = 1 # 방문 체크
            q.append((nr,nc,d+1)) # 큐에 넣기
print(ans)
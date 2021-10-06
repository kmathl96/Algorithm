# 구슬 탈출 2
# 구현, BFS

from collections import deque

N,M = map(int,input().split()) # 보드의 세로 크기와 가로 크기
board = list(input() for _ in range(N)) # 보드의 모양
ans = -1 # 빨간 구슬을 빼내는 최소 횟수

# 빨간 구슬과 파란 구슬의 위치 찾기
for r in range(N):
    for c in range(M):
        if board[r][c] == 'R': r_loc = [r,c]
        if board[r][c] == 'B': b_loc = [r,c]

dr,dc = [-1,0,1,0],[0,1,0,-1]
q = deque([(r_loc,b_loc,0)]) # 큐
visited = [(r_loc,b_loc)] # 같은 위치는 다시 방문하지 않도록 체크
while q:
    r,b,d = q.popleft() # 각 구슬의 위치, 보드를 기울인 횟수
    
    # 횟수가 10번이거나 빨간 구슬을 빼낸 최소 횟수를 찾은 경우 종료
    if d == 10 or ans > -1: break
    
    # 사방으로 기울이기
    for i in range(4):
        nrr,nrc = r # 빨간 구슬이 이동할 위치
        nbr,nbc = b # 파란 구슬이 이동할 위치
        r_cnt,b_cnt = 0,0 # 각 구슬이 이동한 칸 수

        # 파란 구슬 이동
        flag = 0 # 파란 구슬이 구멍에 빠지는지 여부
        while True: # 이동할 수 있는 칸까지 이동
            nbr,nbc = nbr+dr[i],nbc+dc[i] # 한 칸 이동
            if board[nbr][nbc] == 'O': # 구멍인 경우 종료
                flag = 1
                break
            if board[nbr][nbc] == '#': break # 벽이면 종료
            b_cnt += 1 # 이동 칸 수 증가
        if flag: continue # 파란 구슬이 구멍에 빠진 경우 실패
        nbr,nbc = nbr-dr[i],nbc-dc[i] # 파란 구슬이 이동한 후의 위치

        # 빨간 구슬 이동
        while True:
            nrr,nrc = nrr+dr[i],nrc+dc[i]
            if board[nrr][nrc] == 'O':
                ans = d+1 # ans을 (현재 기울인 횟수+1)로 변경하고 종료
                break
            if board[nrr][nrc] == '#': break
            r_cnt += 1
        nrr,nrc = nrr-dr[i],nrc-dc[i]

        # 빨간 구슬과 파란 구슬의 위치가 같은 경우
        if nrr == nbr and nrc == nbc:
            # 더 많이 이동한 구슬의 위치를 한 칸 전으로 변경
            if r_cnt > b_cnt: nrr,nrc = nrr-dr[i],nrc-dc[i]
            else: nbr,nbc = nbr-dr[i],nbc-dc[i]
        
        # 방문했던 위치가 아닌 경우 큐에 넣기
        if ([nrr,nrc],[nbr,nbc]) not in visited:
            visited.append(([nrr,nrc],[nbr,nbc]))
            q.append(([nrr,nrc],[nbr,nbc],d+1))
print(ans)
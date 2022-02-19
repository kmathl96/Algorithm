# 어른 상어
# 구현, 시뮬레이션

from collections import deque

N,M,k = map(int,input().split()) # 격자의 크기

# 격자의 각 칸에 [상어 번호, 상어가 뿌린 냄새의 남은 유지 시간]을 저장
board = [list(map(lambda x: [int(x),0],input().split())) for _ in range(N)]

dirs = list(map(int,input().split())) # 상어의 방향
dr,dc = [0,-1,1,0,0],[0,0,0,-1,1] # 방향 리스트 (상하좌우)
priorities = [list(map(int,input().split())) for _ in range(M*4)] # 방향 우선순위

# 격자에 존재하는 상어들의 정보 저장
sharks = []
for r in range(N):
    for c in range(N):
        if board[r][c][0]:
            sharks.append((board[r][c][0],r,c))
            board[r][c][1] = k # 냄새를 저장
sharks = deque(sorted(sharks)) # 번호 순으로 정렬하여 큐로 변환

# # 1번 상어만 격자에 남을 때까지 상어 이동
t = 0 # 걸리는 시간
while t < 1000 and len(sharks)>1: # 1000초가 넘거나 1번 상어만 남으면 종료
    t += 1 # 1초마다 이동

    # 상어 이동
    for _ in range(len(sharks)):
        num,r,c = sharks.popleft() # 이동할 상어의 번호와 현재 위치
        sr,sc = -1,-1 # 이동할 위치

        # 방향에 맞는 우선순위에 따라 탐색
        for d in priorities[4*(num-1)+dirs[num-1]-1]:
            nr,nc = r+dr[d],c+dc[d] # 탐색할 위치
            if 0<=nr<N and 0<=nc<N:
                # 상어의 이동 방향 결정
                # 1. 아무 냄새가 없는 칸의 방향
                # 2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향
                if not board[nr][nc][0] or sr==-1 and board[nr][nc][0]==num:
                    sr,sc,sd = nr,nc,d # 상어가 이동할 위치와 방향 저장

                    # 아무 냄새가 없는 칸인 경우 더 탐색할 필요가 없으므로 종료
                    if not board[nr][nc][0]: break
        
        # 이동할 위치를 결정했다면, 
        if sr!=-1:
            sharks.append((num,sr,sc))
            dirs[num-1] = sd
    
    # 냄새 뿌리기
    for _ in range(len(sharks)):
        num,r,c = sharks.popleft() # 현재 상어의 번호와 위치

        # 해당 칸에 앞 번호의 상어가 이미 있으므로 격자 밖으로 쫓겨남
        if board[r][c][1] == k+1: continue

        # 현재 상어의 정보를 저장
        board[r][c] = [num,k+1] # 냄새를 감소시킬 것이므로 k보다 1 큰 값으로 저장
        sharks.append((num,r,c))
    
    # 냄새의 유지 시간 감소시키기
    for r in range(N):
        for c in range(N):
            if board[r][c][1]:
                board[r][c][1] -= 1

                # 냄새가 완전히 사라졌으면, 냄새를 뿌린 상어의 번호 지우기
                if not board[r][c][1]: board[r][c][0] = 0

# 1번 상어만 격자에 남게 되기까지 걸리는 시간 출력
# 1000초가 넘어도 다른 상어가 격자에 남아 있으면 -1 출력
print(t if t<=1000 and len(sharks)==1 else -1)
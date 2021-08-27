# 숨바꼭질 2
# BFS

from collections import deque

N,K = map(int,input().split()) # 수빈이와 동생의 위치

# 수빈이가 가는 데 걸리는 가장 빠른 시간과 그 방법의 수
board = [[-1,0] for _ in range(100001)]

q = deque([N]) # 큐
board[N] = [0,1] # 본인의 위치 : 0초, 1가지
while q:
    x = q.popleft() # 현재 위치
    for nx in [x-1,x+1,2*x]: # 걷거나 순간이동을 하는 위치
        if 0<=nx<100001: # 유효한 위치인 경우
            # 1. 아직 간 적 없는 위치인 경우
            if board[nx][0] == -1:
                # 현재 위치에서 이동하는 시간과 그 방법의 수로 변경
                board[nx] = [board[x][0]+1,board[x][1]]
                q.append(nx) # 큐에 넣기
            # 2. 이동할 위치로 가는 데 걸리는 최소 시간이랑 동일하게 걸리는 경우
            elif board[nx][0] == board[x][0]+1:
                board[nx][1] += board[x][1] # 방법의 수를 더함

print(board[K][0]) # 수빈이가 동생을 찾는 가장 빠른 시간
print(board[K][1]) # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수
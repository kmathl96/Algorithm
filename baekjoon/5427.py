# 불
# BFS

import sys
input = sys.stdin.readline

def sol():
    q = [] # 큐
    visited = [[0]*w for _ in range(h)] # 방문 배열
    for r in range(h):
        for c in range(w):
            # @인 경우, 상근이의 시작 위치 저장
            if board[r][c] == '@':
                sr,sc = r,c
            # *인 경우, 불의 위치 좌표를 큐에 넣기
            elif board[r][c] == '*':
                visited[r][c] = 1 # 방문 체크
                q.append((r,c,1)) # 위치 좌표와 불(1) 표시
    
    # 상근이의 위치를 큐에 넣기
    # (불을 먼저 처리하기 위해 상근이의 위치를 나중에 넣어줌)
    visited[sr][sc] = 1 # 상근이의 위치도 방문 체크
    q.append((sr,sc,0)) # 위치 좌표와 불이 아님(0)을 표시
    
    # BFS
    t = 1
    while q:
        new_q = [] # 새로운 큐 : 다음에 탐색할 좌표들 넣기

        # 큐를 순서대로 탐색
        for r,c,is_fire in q:
            # 불이 아니며(=상근이이며) 빌딩 지도의 가장자리에 위치한 경우, 빌딩 탈출
            if not is_fire and (r in (0,h-1) or c in (0,w-1)):
                return str(t) # 빌딩을 탈출하는 데 걸린 시간 반환

            # 인접한 칸 탐색
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i] # 이동할 위치
                # 유효한 위치이며, 방문하지 않았고, 빈 공간인 경우 => 불이나 상근이가 이동할 수 있음
                if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and board[nr][nc]=='.':
                    visited[nr][nc] = 1 # 방문 체크
                    new_q.append((nr,nc,is_fire)) # 나중에 더 탐색하기 위해 큐에 넣기
        q = new_q # 다음에 탐색하기 위해 다시 큐에 저장
        t += 1 # 시간 증가
    
    # 빌딩을 탈출하지 못한 경우, 'IMPOSSIBLE' 반환
    return 'IMPOSSIBLE'

ans = [] # 각 테스트 케이스의 결과를 담을 리스트
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
for _ in range(int(input())): # 입력된 테스트 케이스의 수만큼 반복
    w,h = map(int,input().split()) # 빌딩 지도의 너비와 높이
    board = [list(input().rstrip()) for _ in range(h)] # 빌딩의 지도
    ans.append(sol())

print('\n'.join(ans))
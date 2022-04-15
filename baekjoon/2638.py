# 치즈
# DFS

import sys
input = sys.stdin.readline

def sol():
    N,M = map(int,input().split()) # 모눈종이의 크기
    board = [list(map(int,input().split())) for _ in range(N)] # 모눈종이의 상태
    cnt = sum(sum(row) for row in board) # 치즈의 크기
    dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
    t = 0 # 시간

    # 치즈가 모두 녹아 없어질 때까지 반복
    while cnt:
        t += 1 # 시간 증가
        st = [(0,0)] # 스택
        visited = [[0]*M for _ in range(N)] # 방문 여부, 외부 공기와 접촉하는 변의 개수 체크
        visited[0][0] = 1 # 시작점 방문 표시
        while st:
            r,c = st.pop() # 현재 위치 좌표

            # 사방 탐색
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i] # 탐색할 위치 좌표

                # 유효한 위치인 경우
                if 0<=nr<N and 0<=nc<M:
                    # 치즈가 있는 경우
                    if board[nr][nc]:
                        # 치즈가 있는 칸의 외부 공기 접촉 변의 개수 증가
                        visited[nr][nc] += 1

                        # 외부 공기 접촉 변의 개수가 2인 경우
                        if visited[nr][nc] == 2:
                            board[nr][nc] = 0 # 치즈가 녹아 없어짐
                            cnt -= 1 # 치즈 크기 감소
                    
                    # 치즈가 없고 아직 방문하지 않은 경우 => 외부 공기
                    elif not visited[nr][nc]:
                        visited[nr][nc] = 1
                        st.append((nr,nc))
    print(t)

sol()
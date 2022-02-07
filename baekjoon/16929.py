# Two Dots
# DFS

N,M = map(int,input().split()) # 게임판의 크기
board = [input() for _ in range(N)] # 게임판의 상태
cycle = 0 # 사이클의 존재 여부
visited = [[0]*M for _ in range(N)] # 방문 배열
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향

# 순서대로 탐색
for row in range(N):
    for col in range(M):
        st = [(row,col,1)] # 스택
        while st:
            r,c,d = st.pop() # 현재 위치와 깊이
            if visited[r][c]: continue # 이미 방문한 경우, 더 탐색하지 않음
            visited[r][c] = d # 방문 체크
            
            # 사방 탐색
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i] # 이동할 위치

                # 유효한 위치이며 같은 색깔인 경우
                if 0<=nr<N and 0<=nc<M and board[row][col]==board[nr][nc]:
                    # 아직 방문하지 않은 경우, 스택에 넣고 더 탐색하기
                    if not visited[nr][nc]:
                        st.append((nr,nc,d+1))
                    # 3번 이상 전에 방문한 칸인 경우, 이 칸과 연결하면 사이클이 됨
                    elif d-visited[nr][nc]>=3:
                        cycle = 1
                        break
            
            # 존재하면 더 탐색할 필요가 없으므로 모든 반복문 종료
            if cycle: break
        if cycle: break
    if cycle: break

print("Yes" if cycle else "No") # 존재하면 Yes, 아니면 No 출력
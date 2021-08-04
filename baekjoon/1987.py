# 알파벳
# DFS, 백트래킹

R,C = map(int,input().split()) # 보드의 행/열 길이
board = [list(input()) for _ in range(R)] # 보드의 각 칸에 적혀있는 알파벳
ans = 1 # 말이 지날 수 있는 칸의 수의 최댓값
dr,dc = [-1,0,1,0],[0,1,0,-1]

# DFS
st = [(0,0,1,board[0][0])] # 스택
while st:
    r,c,d,s = st.pop() # 현재 위치와 지나온 칸의 개수, 지나온 칸의 알파벳
    if d > ans: ans = d # ans 갱신
    # 인접한 칸 탐색
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        # 유효한 위치이며, 해당 알파벳이 지나온 칸에 있지 않은 경우
        if 0<=nr<R and 0<=nc<C and board[nr][nc] not in s:
            st.append((nr,nc,d+1,s+board[nr][nc])) # 스택에 넣기
print(ans)
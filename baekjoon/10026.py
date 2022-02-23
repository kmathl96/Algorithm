# 적록색약
# DFS

dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향

# 같은 구역 찾기
def dfs(row,col):
    global visited
    visited[row][col] = 1
    st = [(row,col)] # 스택에 위치 넣기
    while st:
        r,c = st.pop()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치
            
            # 유효한 위치이며 아직 방문하지 않았고 같은 색상인 경우, 더 탐색
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and grid[row][col]==grid[nr][nc]:
                visited[nr][nc] = 1
                st.append((nr,nc))

N = int(input()) # 그리드의 크기
grid = [list(input()) for _ in range(N)] # 그리드의 상태

# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수 구하기
ans = [0,0] # 각각의 구역의 수
for i in range(2):
    visited = [[0]*N for _ in range(N)] # 방문 배열
    for r in range(N):
        for c in range(N):
            # 아직 방문하지 않은 배열이라면 탐색(같은 구역 찾기) 수행
            if not visited[r][c]:
                dfs(r,c)
                ans[i] += 1 # 구역의 수 하나 증가
            
            # 다음에 적록색약인 사람의 경우를 처리할 수 있도록 G를 R로 변경
            if grid[r][c]=='G': grid[r][c] = 'R'
print(*ans)
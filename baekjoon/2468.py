# 안전 영역
# 브루트포스, DFS

# 지역 탐색 및 물의 높이 1 증가
def dfs(r,c):
    global visited,area
    visited[r][c] = 1 # 방문 체크
    area[r][c] -= 1 # 물의 높이 증가 => 높이 1 감소

    # 지역 탐색
    st = [(r,c)] # 스택
    while st:
        r,c = st.pop() # 현재 위치
        # 사방 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치

            # 유효한 위치이며 아직 잠기지 않았고 방문하지 않은 지역인 경우
            if 0<=nr<N and 0<=nc<N and area[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1 # 방문 체크
                area[nr][nc] -= 1 # 높이 감소
                st.append((nr,nc)) # 더 탐색하기 위해 스택에 넣기

N = int(input()) # 지역의 크기
area = [list(map(int,input().split())) for _ in range(N)] # 높이 정보
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
ans = 0 # 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수

# 지역의 최대 높이 만큼 비가 내릴 때까지 반복
for _ in range(max(max(row for row in area))):
    visited = [[0]*N for _ in range(N)] # 방문 배열
    cnt = 0 # 안전 영역의 개수
    for r in range(N):
        for c in range(N):
            # 아직 잠기지 않았으며 방문하지 않은 지역인 경우 탐색
            if area[r][c] and not visited[r][c]:
                dfs(r,c)
                cnt += 1 # 안전 영역 개수 증가
    ans = max(ans,cnt) # ans 갱신
print(ans)
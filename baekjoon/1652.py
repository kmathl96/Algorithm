# 누울 자리를 찾아라
# 구현, 문자열

N = int(input()) # 방의 크기
room = [input() for _ in range(N)] # 방의 구조
ans = [0,0] # 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수
dr,dc = [0,1],[1,0] # 방향 배열 : 가로로 탐색, 세로로 탐색

# 가로와 세로 순서대로 탐색
for i in range(2):
    visited = [[0]*N for _ in range(N)] # 중복 탐색 방지

    # 방의 각 칸을 탐색
    for r in range(N):
        for c in range(N):
            # 이미 탐색했거나 짐이 있는 칸인 경우 탐색하지 않음
            if visited[r][c] or room[r][c]=='X': continue

            # 누울 수 있는지 탐색
            visited[r][c] = 1 # 방문 체크
            flag = 0 # 누울 수 있는지 여부
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치

            # 유효한 위치이며 빈 칸인 경우
            while nr<N and nc<N and room[nr][nc]=='.':
                visited[nr][nc] = 1 # 방문 체크
                nr,nc = nr+dr[i],nc+dc[i] # 다음 칸 탐색
                flag = 1 # 여부 변경
            
            # 누울 수 있는 경우
            if flag:
                ans[i] += 1 # 자리의 개수 증가

print(*ans)
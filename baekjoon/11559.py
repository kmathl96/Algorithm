# Puyo Puyo
# 구현, DFS, 시뮬레이션

def dfs(row,col,val):
    st = [(row,col)] # 스택
    visited[row][col] = 1 # 방문 체크
    group = [(row,col)] # 뿌요 그룹
    while st:
        r,c = st.pop()

        # 인접한 칸 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 확인할 위치
            # 유효한 위치이며, 아직 방문하지 않았고, 같은 색인 경우
            if 0<=nr<6 and 0<=nc<12 and not visited[nr][nc] and field[nr][nc]==val:
                visited[nr][nc] = 1 # 방문 체크
                st.append((nr,nc)) # 더 탐색하기 위해 스택에 넣기
                group.append((nr,nc)) # 뿌요 그룹에 추가
    return group

field = [list(input()) for _ in range(12)] # 필드의 정보
field = [[field[11-r][c] for r in range(12)] for c in range(6)] # 필드를 시계방향으로 90도 돌림
ans = 0 # 연쇄가 연속으로 일어나는 횟수
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열

# 연쇄가 끝날 때까지 반복
while True:
    visited = [[0]*12 for _ in range(6)] # 방문 배열
    remove = [] # 없어질 뿌요의 좌표

    # 뿌요 그룹(연결된 같은 색 뿌요들) 찾기
    for r in range(6):
        for c in range(12):
            # 빈 공간이 아니며 아직 방문하지 않은 곳인 경우
            if field[r][c]!='.' and not visited[r][c]:
                group = dfs(r,c,field[r][c]) # 뿌요 그룹

                # 뿌요들이 4개 이상인 경우, 터지게 됨
                if len(group) >= 4:
                    remove += group # 없앨 뿌요에 추가함
    
    # 없어지는 뿌요가 없는 경우, 연쇄가 일어나지 않는 것이므로 종료
    if not remove: break

    # 뿌요 없어짐
    for r,c in remove:
        field[r][c] = '.' # 빈 칸으로 저장
    
    # 뿌요가 아래로 떨어짐
    for r in range(6):
        # 끝 열부터 탐색
        for c in range(11,-1,-1):
            # 빈 칸인 경우
            if field[r][c] == '.':
                # 해당 칸을 없애고 맨끝 열에 빈 칸 넣기
                field[r].append(field[r].pop(c))
    
    ans += 1 # 연쇄 횟수 증가
print(ans)
# 상어 중학교
# 구현, 시뮬레이션, DFS

# 블록 그룹 찾기
def dfs(row,col):
    global B,rainbow,pos
    visited[row][col] = flag # 방문 체크
    st = [(row,col)] # 스택
    size,cnt0 = 0,0 # 블록 그룹의 크기, 무지개 블록(0)의 개수
    while st:
        r,c = st.pop()
        size += 1 # 크기 증가
        
        # 인접한 칸 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 칸
            # 유효한 위치이며, 이번 탐색 때 아직 방문하지 않은 경우
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]!=flag:
                # 무지개 블록인 경우
                if not board[nr][nc]:
                    cnt0 += 1 # 무지개 블록의 개수 증가
                # 같은 색이 아닌 경우, 탐색할 필요가 없음
                elif board[nr][nc] != board[row][col]: continue
                visited[nr][nc] = flag # 방문 체크
                st.append((nr,nc)) # 스택에 넣기
    
    # 제거할 블록 그룹 갱신
    # 1) 크기가 더 크거나
    # 2) 크기가 같다면, 무지개 블록의 수가 더 많거나
    # 3) 무지개 블록의 수도 같다면, 기준 블록의 행보다 행이 더 크거나
    # 4) 기준 블록의 행과 같은 행이라면, 기준 블록의 열보다 열이 더 큰 경우
    if B<size or (B==size and (rainbow<cnt0 or (rainbow==cnt0 and (pos[0]<row or pos[0]==row and pos[1]<col)))):
        # 크기, 무지개 블록의 수, 기준 블록의 위치 저장
        B = size
        rainbow = cnt0
        pos = row,col

# 블록 제거
def remove(row,col):
    global board
    st = [(row,col)] # 스택
    val = board[row][col] # 블록 그룹의 색
    board[row][col] = -2 # 제거 : -2로 표시
    while st:
        r,c = st.pop() # 탐색할 블록
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 인접한 칸
            # 유효한 위치이며, 무지개 블록이거나 같은 색의 블록인 경우
            if 0<=nr<N and 0<=nc<N and board[nr][nc] in (0,val):
                board[nr][nc] = -2 # 제거
                st.append((nr,nc)) # 스택에 넣기

# 중력 작용
def gravity():
    # 열을 차례대로 탐색
    for c in range(N):
        # 맨밑 행부터 탐색
        r = N
        while r:
            r -= 1
            
            # 비어있지 않은 경우, 넘어감
            if board[r][c] != -2: continue
            
            # 바로 윗행부터 역순으로 탐색
            for idx in range(r-1,-1,-1):
                # 비어있는 경우, 윗칸을 탐색하기 위해 넘어감
                if board[idx][c] == -2: continue

                # 검은색 블록이 아닌 경우
                if board[idx][c] >= 0:
                    board[r][c] = board[idx][c] # 해당 블록이 내려감
                    board[idx][c] = -2 # 해당 블록의 위치는 비어있다고 표시
                
                # 블록이 내려갔거나, 검은색 블록(고정되어있음)이므로 종료
                break

N,M = map(int,input().split()) # 격자 한 변의 크기, 색상의 개수
board = [list(map(int,input().split())) for _ in range(N)] # 블록의 정보
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
score = 0 # 획득한 점수의 합
flag = 1 # 블록 그룹의 개수 (방문 배열 체크할 때 그룹을 구분하기 위함)

# 오토 플레이 반복
while True:
    # 1. 크기가 가장 큰 블록 그룹 찾기
    B,rainbow = 1,0 # 블록 그룹의 크기, 무지개 블록의 수
    visited = [[0]*N for _ in range(N)] # 방문 배열
    pos = 0,0 # 기준 블록
    for r in range(N):
        for c in range(N):
            # 기본 블럭이면서 아직 방문하지 않은 경우, 블록 그룹 찾기
            if board[r][c]>0 and not visited[r][c]:
                dfs(r,c)
                flag += 1
    # 블록 그룹(크기가 2 이상이어야 함)이 존재하지 않는 경우, 종료
    if B == 1: break

    # 2. 1에서 찾은 블록 그룹의 모든 블록 제거
    remove(pos[0],pos[1])
    score += B**2 # 점수 획득

    # 3. 격자에 중력 작용
    gravity()

    # 4. 격자가 90도 반시계 방향으로 회전
    board = [[board[r][N-1-c] for r in range(N)] for c in range(N)]
    
    # 5. 다시 격자에 중력 작용
    gravity()

print(score)
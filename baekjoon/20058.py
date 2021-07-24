# 마법사 상어와 파이어스톰
# 구현, DFS, 시뮬레이션

# 부분 격자를 회전
def rot(row,col,size):
    # temp 리스트에 회전한 값을 저장
    temp = [[0]*size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            temp[r][c] = A[row+size-1-c][col+r]
    # temp 그대로 다시 A에 저장
    for r in range(size):
        for c in range(size):
            A[row+r][col+c] = temp[r][c]

# 연결되어 있는 칸 찾기
def dfs(r,c):
    global cnt
    A[r][c] = 0 # 더 탐색하지 않도록 0으로 변경
    st = [(r,c)] # 스택
    temp = 1 # 덩어리가 차지하는 칸의 개수
    while st:
        r,c = st.pop() # 현재 위치
        # 인접한 칸 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            # 유효한 위치이며, 얼음이 있는 경우
            if 0<=nr<n and 0<=nc<n and A[nr][nc]:
                st.append((nr,nc)) # 스택에 넣기
                A[nr][nc] = 0 # 더 탐색하지 않도록 0으로 변경
                temp += 1 # 덩어리가 차지하는 칸의 개수 증가
    if cnt < temp: cnt = temp # cnt 갱신

N,Q = map(int,input().split()) # 격자의 크기(2^N)와 상어가 시전한 단계의 개수
n = 2**N # 격자의 크기
A = [list(map(int,input().split())) for _ in range(n)] # 각 칸에 있는 얼음의 양
L = list(map(int,input().split())) # 각 단계 정보
dr,dc = [-1,0,1,0],[0,1,0,-1]
for l in L:
    size = 2**l # 부분 격자의 크기

    # 모든 부분 격자를 시계방향으로 90도 회전
    for r in range(0,n,size):
        for c in range(0,n,size):
            rot(r,c,size)
    
    # 인접한 얼음 칸이 3개 미만인 경우, 얼음 양 감소
    removed = [] # 얼음 양이 감소될 좌표
    for r in range(n):
        for c in range(n):
            if not A[r][c]: continue # 얼음이 없는 경우, 넘어감
            cnt = 0 # 인접하면서 얼음이 있는 칸의 개수
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i]
                # 인접한 좌표가 유효한 위치이며 얼음이 있는 경우, 개수 증가
                if 0<=nr<n and 0<=nc<n and A[nr][nc]: cnt += 1
                if cnt > 2: break # 개수가 3 이상이면 종료
            # 개수가 3 미만인 경우 감소할 얼음 리스트에 추가
            if cnt < 3: removed.append((r,c))
    # 얼음의 양이 1 줄어듦
    for r,c in removed:
        A[r][c] -= 1

# 1. 남아있는 얼음의 합
print(sum(map(sum,A)))

# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
cnt = 0
for r in range(n):
    for c in range(n):
        # 얼음이 있는 칸인 경우, dfs로 덩어리 탐색
        if A[r][c]: dfs(r,c)
print(cnt)
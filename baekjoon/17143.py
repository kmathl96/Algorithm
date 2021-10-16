# 낚시왕
# 구현, 시뮬레이션

dr,dc = [-1,1,0,0],[0,0,1,-1]
def move(): # 상어 이동
    global board
    new = [[0]*C for _ in range(R)] # 상어들이 이동한 위치를 저장할 격자판
    for r,c,s,d,z in sharks:
        nr,nc = r+dr[d-1]*s,c+dc[d-1]*s # 이동할 위치
        
        # 유효한 위치가 아닌 경우, 좌표 조정하기
        if not 0<=nr<R:
            nr = abs(nr) # 절대값으로 바꿈
            if ((nr-1)//(R-1))&1: # 아래 경계를 넘어감
                d = 1 # 위 방향으로 변경
                nr = R-2-(nr-1)%(R-1) # 이동할 좌표 변경
            else: # 위 경계를 넘어감
                d = 2 # 아래 방향으로 변경
                nr = (nr-1)%(R-1)+1
        elif not 0<=nc<C:
            nc = abs(nc)
            if ((nc-1)//(C-1))&1: # 오른쪽 경계를 넘어감
                d = 4 # 왼쪽 방향으로 변경
                nc = C-2-(nc-1)%(C-1)
            else: # 왼쪽 경계를 넘어감
                d = 3 # 오른쪽 방향으로 변경
                nc = (nc-1)%(C-1)+1
        
        # 상어가 없거나, 자신보다 크기가 작은 상어가 있는 경우
        if not new[nr][nc] or new[nr][nc][2] < z:
            new[nr][nc] = (s,d,z) # 해당 칸으로 이동
    board = new # 격자판 갱신

R,C,M = map(int,input().split()) # 격자판의 크기와 상어의 수
board = [[0]*C for _ in range(R)] # 격자판
for _ in range(M):
    r,c,s,d,z = map(int,input().split()) # 상어의 위치와 속력, 이동 방향, 크기
    board[r-1][c-1] = (s,d,z) # 위치에 맞는 좌표에 정보 넣기

ans = 0 # 낚시왕이 잡은 상어 크기의 합
for loc in range(C): # 1. 낚시왕 이동
    # 상어 찾기
    sharks = []
    flag = 0 # 상어를 잡았는지 여부
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                # 2. 상어 잡기
                if c==loc and not flag: # 같은 열에 있으며 아직 상어를 안 잡은 경우
                    ans += board[r][loc][2] # 상어의 크기만큼 ans 증가
                    board[r][loc] = 0 # 상어가 사라짐
                    flag = 1
                    continue
                s,d,z = board[r][c] # 상어의 속력, 이동 방향, 크기
                sharks.append((r,c,s,d,z)) # 상어의 위치와 정보 넣기
    move() # 3. 상어 이동
print(ans)
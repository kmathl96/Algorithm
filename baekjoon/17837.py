# 새로운 게임 2
# 구현, 시뮬레이션

N,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
pieces = [] # 각 말의 위치와 방향
chess = [[[] for i in range(N)] for j in range(N)] # 현재 체스판 상태 : r행 c열에 위치한 말
# 체스판 초기화
for k in range(K):
    r,c,d = map(int,input().split())
    # 문제에서 주어진 행/열 값을 배열 인덱스에 맞도록 바꿔서 넣음
    # 방향도 마찬가지
    # r => r-1, c => c-1, d => d-1
    pieces.append((r-1,c-1,d-1))
    chess[r-1][c-1].append(k)
dr,dc = [0,0,-1,1],[1,-1,0,0] # 방향 리스트 : 오른쪽, 왼쪽, 위쪽, 아래쪽
isEnd = 0 # 턴 중간에 끝났을 경우 게임을 끝내기 위한 변수
cnt = 0 # 턴 횟수
while cnt<1001 and not isEnd:
    for i in range(K):
        r,c,d = pieces[i] # i번째 말의 위치와 방향
        nr,nc = r+dr[d],c+dc[d] # i 말이 이동할 위치
        # 이동할 칸이 체스판 밖이거나 파란색인 경우
        if not (0<=nr<N and 0<=nc<N) or board[nr][nc]==2:
            nr,nc = r-dr[d],c-dc[d] # 반대 방향으로 이동
            if d&1: d -= 1 # 1(왼쪽)=>0(오른쪽), 3(아래쪽)=>2(위쪽)
            else: d += 1 # 0(오른쪽)=>1(왼쪽), 2(위쪽)=>3(아래쪽)
            # 이동할 칸이 체스판 밖이거나 파란색인 경우 안 움직임
            if not (0<=nr<N and 0<=nc<N) or board[nr][nc]==2:
                pieces[i] = (r,c,d) # 바뀐 방향으로 말 상태 갱신
                continue
        # 자신과 자신 위에 올려져 있는 말들의 상태(위치, 방향) 갱신
        idx = chess[r][c].index(i) # 자신이 있는 위치에서 어느 높이에 있는지
        move = chess[r][c][idx:] # 자신 위에 올려져 있는 말들까지 움직임
        for p in move: # 옮길 말들의 상태 갱신
            pieces[p] = (nr,nc,pieces[p][2]) # 새 위치로 자신의 방향을 유지한 채 이동
        pieces[i] = (nr,nc,d) # d값이 바뀌었을 수도 있으므로 i 말의 상태 갱신
        # 이동할 칸이 빨간색인 경우, 이동할 말들의 순서를 뒤집어서 이동
        if board[nr][nc]==1: move = move[::-1]
        # 새 위치에 말들을 옮기고, 원래 위치에서 제거
        chess[nr][nc] += move
        chess[r][c] = chess[r][c][:idx]
        if len(chess[nr][nc])>3: # 4개 이상 쌓인 경우 게임 종료
            isEnd = 1
            break
    cnt += 1
print(cnt if cnt<1001 else -1)
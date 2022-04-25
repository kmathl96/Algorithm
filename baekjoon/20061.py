# 모노미노도미노 2
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

# 보드에 블록 놓기
def move(t,pos,board):
    put = 0 # 경계를 만나기 전까지 블록을 놓았는지 여부
    
    # 1*1 블록 놓기
    if t == 1:
        # 블록이 이동하는 순서대로 확인
        for c in range(5):
            # 다음 열에 타일이 있는 경우, 현재 위치에 블록 놓기
            if board[pos][c+1]:
                board[pos][c] = 1
                put = 1
                break

        # 경계를 만나기 전까지 못 놓은 경우, 마지막 열에 놓기
        if not put: board[pos][5] = 1
    
    # 1*2 블록 놓기
    if t == 2:
        for c in range(4):
            # 다다음 열에 타일이 있는 경우, 현재 위치에 블록 놓기
            if board[pos][c+2]:
                board[pos][c] = 1
                board[pos][c+1] = 1
                put = 1
                break
        if not put:
            board[pos][4] = 1
            board[pos][5] = 1
    
    # 2*1 블록 놓기
    if t == 3:
        for c in range(5):
            # 다음 열에 타일이 하나라도 있는 경우, 현재 위치에 블록 놓기
            if board[pos][c+1] or board[pos+1][c+1]:
                board[pos][c] = 1
                board[pos+1][c] = 1
                put = 1
                break
        if not put:
            board[pos][5] = 1
            board[pos+1][5] = 1
    return board

# 타일 제거
def remove(board):
    global score

    # 1. 타일 이동 및 제거
    col = 5 # 탐색할 열
    for _ in range(6): # 6번 확인 (열이 6개이므로)
        flag = 1 # 해당 열이 타일로 가득 차있는지 여부
        for r in range(4):
            # 해당 칸이 비어있는 경우, 더 탐색하지 않고 종료
            if not board[r][col]:
                flag = 0
                break
        
        # 타일로 가득 차있다면, 모두 사라지고 나머지 타일이 이동함
        if flag:
            for r in range(4):
                for c in range(col,0,-1):
                    board[r][c] = board[r][c-1] # 이전 열의 타일 존재 여부 저장
                board[r][0] = 0 # 첫 열은 새로 생기므로 0 저장
            score += 1 # 점수 획득
        # 비어있는 칸이 있다면, 타일이 사라지지 않으므로 이전 열을 탐색해야 함
        else: col -= 1
    
    # 2. 특별한 칸(0, 1번 열) 처리
    cnt = 0 # 블록이 있는 열의 수
    for c in range(2):
        for r in range(4):
            # 블록이 있는 경우, 해당 행은 탐색 종료
            if board[r][c]:
                cnt += 1 # 개수 증가
                break
    # 블록이 있는 열의 수만큼 타일 제거
    for _ in range(cnt):
        for r in range(4):
            for c in range(5,0,-1):
                board[r][c] = board[r][c-1] # 이전 열의 타일 존재 여부 저장
            board[r][0] = 0 # 첫 열은 새로 생기므로 0 저장
    return board

N = int(input()) # 블록을 놓은 횟수
score = 0 # 점수
boardB = [[0]*6 for _ in range(4)] # 파란색 보드
boardG = [[0]*6 for _ in range(4)] # 초록색 보드
for _ in range(N):
    t,x,y = map(int,input().split()) # 블록을 놓은 정보 : 블록의 종류와 좌표
    boardB = remove(move(t,x,boardB)) # 파란색 보드 처리
    if t==2: y += 1 # 초록색 보드에서의 좌표 처리
    boardG = remove(move((4-t)%3+1,3-y,boardG)) # 초록색 보드 처리

# 블록을 모두 놓았을 때 얻은 점수
print(score)

# 파란색 보드와 초록색 보드에서 타일이 들어있는 칸의 개수
print(sum(sum(row) for row in boardB)+sum(sum(row) for row in boardG))
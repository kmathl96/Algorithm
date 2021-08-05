# 스도쿠
# 백트래킹, DFS

# 해당 칸에 해당 숫자가 들어갈 수 있는지 확인
# 특정 구역에 같은 숫자가 있으면 0 반환하고 바로 종료
def check(r,c,num):
    # 같은 행에 숫자가 있는지 확인
    if num in board[r]: return 0
    # 같은 열에 숫자가 있는지 확인
    for i in range(9):
        if board[i][c] == num: return 0
    # 3*3 정사각형 안에 숫자가 있는지 확인
    for i in range(r//3*3,r//3*3+3):
        for j in range(c//3*3,c//3*3+3):
            if board[i][j] == num: return 0
    return 1 # 행, 열, 정사각형 안에 같은 숫자가 없는 경우 1 반환

# d번째 빈 칸 채우기
def sudoku(d):
    global isEnd
    if isEnd: return # 다 채운 경우 종료

    # 다 채운 경우, 스도쿠 판 출력 후 종료
    if d == len(empty):
        for row in board: print(*row) # 스도쿠 판 출력
        isEnd = 1 # 다 채워졌으므로 변경
        return
    
    # 칸 채우기
    r,c = empty[d] # 채울 빈 칸의 위치
    for num in range(1,10): # 1~9를 채울 수 있는지 확인
        if check(r,c,num):
            board[r][c] = num # 해당 숫자로 채우기
            sudoku(d+1) # 그다음 빈 칸 채우기
            board[r][c] = 0 # 다시 0으로 변경

# 스도쿠 판 각 칸에 쓰여 있는 숫자
board = [list(map(int,input().split())) for _ in range(9)]

# 빈 칸 찾기
empty = []
for r in range(9):
    for c in range(9):
        if not board[r][c]: empty.append((r,c))

isEnd = 0 # 스도쿠판을 다 채웠는지
sudoku(0) # 0번째 빈 칸부터 채우기 시작
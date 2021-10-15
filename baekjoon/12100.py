# 2048 (Easy)
# 구현, 브루트포스, 시뮬레이션, 백트래킹

from copy import deepcopy

# 보드 90도 회전
def rotate(arr):
    return [[arr[N-1-c][r] for c in range(N)] for r in range(N)]

# 왼쪽 방향으로 이동
def move(board):
    arr = deepcopy(board) # 원래 보드에 영향을 주지 않도록 복사
    for r in range(N):
        # 해당 행에 있는 0을 모두 오른쪽으로 이동시킴
        for c in range(N-1,-1,-1):
            if not arr[r][c]: arr[r].append(arr[r].pop(c))
        
        for c in range(N-1):
            if not arr[r][c]: break # 0이면 종료
            # 다음 칸과 같은 값을 가진 경우 합쳐짐
            if arr[r][c] == arr[r][c+1]:
                arr[r][c] *= 2 # 숫자가 2배로 증가
                arr[r].pop(c+1) # 한 칸 없어지고
                arr[r].append(0) # 뒤에 0칸 추가
    return arr

def game(board,d): # d = 현재까지 이동한 횟수
    global ans

    # 5번 이동한 경우 종료
    if d == 5:
        for r in range(N):
            for c in range(N):
                # 블록의 값이 ans보다 더 큰 경우 변경
                if ans < board[r][c]: ans = board[r][c]
        return
    
    # 네 방향으로 이동
    game(move(board),d+1) # 왼쪽 방향으로 이동
    for _ in range(3): # 나머지 세 방향
        board = rotate(board) # 90도 돌린 후
        game(move(board),d+1) # 왼쪽 방향 이동하고 다음 차례 이동하기

N = int(input()) # 보드의 크기
board = [list(map(int,input().split())) for _ in range(N)] # 보드의 상태
ans = 0 # 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록의 값 초기화
game(board,0) # 이동
print(ans)
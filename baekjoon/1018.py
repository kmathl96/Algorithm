# 체스판 다시 칠하기
# 브루트포스

# (r,c)를 왼쪽 상단 모서리로 하는 8*8 크기의 체스판으로 잘라내서 체스판처럼 칠하기
def find(r,c,val):
    global ans
    cnt = 0 # 다시 칠해야 하는 정사각형의 개수

    # 체스판 탐색
    for i in range(8):
        for j in range(8):
            # 위치에 맞는 색상이 아닌 경우, 다시 칠해야 함
            if ((i+j)&1 and board[r+i][c+j]==val) or (not (i+j)&1 and board[r+i][c+j]!=val):
                cnt += 1 # 개수 증가
    
    # 해당 체스판의 경우의 개수 cnt와
    # 반대 색상으로 칠해진 체스판의 경우의 개수 (64-cnt)과
    # ans를 비교하여, 최솟값으로 갱신
    ans = min(ans,cnt,64-cnt)

N,M = map(int,input().split()) # 보드의 크기
board = [input() for _ in range(N)] # 보드의 상태
ans = 64 # 다시 칠해야 하는 정사각형의 개수 : 체스판의 크기(8*8)로 초기화
for r in range(N-7):
    for c in range(M-7):
        find(r,c,board[r][c])
print(ans)
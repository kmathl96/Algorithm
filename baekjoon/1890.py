# 점프
# 다이나믹 프로그래밍

N = int(input()) # 게임 판의 크기
board = [list(map(int,input().split())) for _ in range(N)] # 각 칸에 적혀져 있는 수
cnts = [[0]*N for _ in range(N)] # 해당 칸에 도착하는 경우의 수
cnts[0][0] = 1 # 이동을 시작할 칸
for r in range(N):
    for c in range(N):
        # 현재 칸에서 갈 수 있는 거리, 현재 칸으로 이동할 수 있는 경우의 수
        d,cnt = board[r][c],cnts[r][c]
        if not cnt or not d: continue # 거리나 경우의 수가 0인 경우 넘어감
        
        # 점프할 수 있는 칸인 경우
        # 점프할 칸의 경우의 수를 현재 칸의 경우의 수만큼 증가
        if r+d < N: cnts[r+d][c] += cnt # 오른쪽으로 점프
        if c+d < N: cnts[r][c+d] += cnt # 아래로 점프
print(cnts[N-1][N-1]) # 마지막 칸으로 이동할 수 있는 경우의 수 출력
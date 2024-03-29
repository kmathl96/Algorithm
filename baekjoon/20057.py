# 마법사 상어와 토네이도
# 구현, 시뮬레이션

def move():
    global ans
    sand = A[r][c] # 해당 칸의 모래의 양
    temp = 0 # 흩날린 모래의 양

    # 각 칸으로 모래 흩날리기
    for i in range(10):
        nr,nc = r+dr[d][i],c+dc[d][i] # 모래가 이동할 칸

        # 흩날릴 모래의 양 정하기
        if i<9:
            ns = int(sand*rate[i]*0.01) # 흩날릴 모래의 양
            temp += ns # 흩날린 모래의 양 증가
        else: ns = sand-temp # a칸으로 이동하는 경우, 남은 모래의 양

        # 모래 이동
        if 0<=nr<N and 0<=nc<N: A[nr][nc] += ns # 흩날린 모래의 양만큼 증가
        else: ans += ns # 유효한 위치가 아닌 경우, 밖으로 나간 모래 양 증가
    A[r][c] = 0 # 모래 제거

N = int(input()) # 격자의 크기
A = [list(map(int,input().split())) for _ in range(N)] # 각 칸에 있는 모래
r,c = N//2,N//2 # 토네이도의 위치

# 방향 리스트
# 비율 순서대로 넣음 + a 위치로의 방향(= 토네이도의 방향)
# (토네이도의 방향 : 좌-하-우-상)
dr = [[-1,1,-2,2,0,-1,1,-1,1,0],[-1,-1,0,0,2,0,0,1,1,1],[-1,1,-2,2,0,-1,1,-1,1,0],[1,1,0,0,-2,0,0,-1,-1,-1]]
dc = [[1,1,0,0,-2,0,0,-1,-1,-1],[-1,1,-2,2,0,-1,1,-1,1,0],[-1,-1,0,0,2,0,0,1,1,1],[-1,1,-2,2,0,-1,1,-1,1,0]]
rate = [1,1,2,2,5,7,7,10,10] # 비율

ans,d,cnt = 0,0,1 # 격자 밖으로 나간 모래의 양, 토네이도의 방향, 해당 방향으로 이동할 칸 수
for _ in range(N//2*4+1): # (방향을 바꾸는 횟수+1) 만큼 반복
    # 해당 방향으로 이동 (cnt 만큼 반복)
    for t in range(cnt):
        r,c = r+dr[d][9],c+dc[d][9] # 토네이도 이동 (a 방향과 같음)
        if A[r][c]: move() # 모래가 있으면 모래 이동
    if d&1: cnt += 1 # 밑 방향이거나 윗 방향이었으면, 이동 횟수 증가
    d = (d+1)%4 # 방향 변경
print(ans)
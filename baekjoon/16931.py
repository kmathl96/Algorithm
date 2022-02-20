# 겉넓이 구하기
# 구현

N,M = map(int,input().split()) # 종이의 크기

# 종이의 각 칸에 놓인 정육면체의 수
# 테두리를 0으로 둘러쌈
cubes = [[0]*(M+2)]+[[0]+list(map(int,input().split()))+[0] for _ in range(N)] + [[0]*(M+2)]

ans = 2*N*M # 도형의 겉넓이 : 윗면과 바닥면의 겉넓이 합으로 초기화 (각 칸에는 정육면체가 1개 이상 놓여있음)

# 모든 칸에 대해서 사방으로 탐색
# 각 방향에서 인접한 칸의 정육면체와의 높이 차이만큼 겉면이 보임
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향
for r in range(1,N+1):
    for c in range(1,M+1):
        # 인접한 칸 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 칸
            # 인접한 칸에 있는 정육면체의 높이가 더 작은 경우
            if cubes[r][c] > cubes[nr][nc]:
                ans += cubes[r][c]-cubes[nr][nc] # 높이 차만큼 더함
print(ans)
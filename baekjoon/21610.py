# 마법사 상어와 비바라기
# 구현, 시뮬레이션

N,M = map(int,input().split()) # 격자의 크기, 구름 이동 명령 횟수
A = [list(map(int,input().split())) for _ in range(N)] # 이동의 정보
dr,dc = [0,0,-1,-1,-1,0,1,1,1],[0,-1,-1,0,1,1,1,0,-1] # 이동 방향
clouds = [(N-2,0),(N-2,1),(N-1,0),(N-1,1)] # 구름의 좌표
for _ in range(M):
    d,s = map(int,input().split()) # 이동 방향과 거리
    removed = set() # 구름이 이동한 좌표 => 나중에 사라짐

    # 1. 모든 구름이 d 방향으로 s칸 이동
    for cr,cc in clouds:
        # 첫행-끝행, 첫열-끝열이 연결되어 있으므로 % 연산으로 좌표를 처리
        nr,nc = (cr+s*dr[d])%N,(cc+s*dc[d])%N
        
        # 2. 비 내림
        A[nr][nc] += 1 # 해당 칸의 물 양 증가
        
        # 3. 구름이 모두 사라짐
        removed.add((nr,nc)) # 이동한 위치 넣기
    
    # 4. 물복사버그
    for rr,rc in removed:
        # 대각선 방향으로 거리가 1인 칸 탐색
        for i in range(4):
            nr,nc = rr+dr[2+2*i],rc+dc[2+2*i]
            # 유효한 위치이며 바구니에 물이 있는 경우, 원래 위치의 물 양 증가
            if 0<=nr<N and 0<=nc<N and A[nr][nc]: A[rr][rc] += 1
    
    # 5. 구름 생김
    clouds = []
    for r in range(N):
        for c in range(N):
            # 물의 양이 2 이상이며, 구름이 사라진 칸이 아닌 경우
            if A[r][c] > 1 and (r,c) not in removed:
                clouds.append((r,c)) # 구름이 생김
                A[r][c] -= 2 # 물의 양 감소

# 바구니에 들어있는 물의 양의 합
print(sum(map(sum,A)))
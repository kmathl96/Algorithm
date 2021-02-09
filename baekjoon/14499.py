# 주사위 굴리기
# 구현, 시뮬레이션

N,M,x,y,K = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(N)]
dice = [0]*6 # 주사위의 각 칸(상단, 북쪽 방향, 동쪽 방향, 서쪽 방향, 남쪽 방향, 하단)에 쓰여 있는 값
d = [(0,1),(0,-1),(-1,0),(1,0)] # 동쪽, 서쪽, 북쪽, 남쪽 이동
for c in map(int,input().split()):
    nx,ny = x+d[c-1][0],y+d[c-1][1] # 주사위가 이동할 칸
    if not (0<=nx<N and 0<=ny<M): continue # 해당 칸이 지도 밖이라면 명령 무시
    # 명령어에 따라 주사위의 각 칸에 있는 수 갱신
    if c==1: dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif c==2: dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
    elif c==3: dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
    else: dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]
    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위 바닥면에 쓰여 있는 수를 해당 칸에 복사
    if not mp[nx][ny]: mp[nx][ny] = dice[5]
    # 0이 아닌 경우, 칸에 쓰여 있는 수를 주사위 바닥면으로 복사, 해당 칸은 0
    else: dice[5],mp[nx][ny] = mp[nx][ny],0
    x,y = nx,ny # 주사위의 위치를 갱신
    print(dice[0]) # 이동할 때마다 주사위 상단 값 출력
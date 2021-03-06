# 두 동전
# 브루트포스
# board를 갱신하지 않는 방식으로 풀어 실행속도 단축

dr,dc = [-1,0,1,0],[0,1,0,-1]
def move(coins, cnt):
    global ans
    if cnt == 10: return # 10번 이상은 실패
    for i in range(4): # 사방으로 움직임
        new_coins = [] # 움직인 동전의 위치 저장
        for r,c in coins:
            nr,nc = r+dr[i],c+dc[i] # 움직인 동전의 좌표
            if 0<=nr<N and 0<=nc<M: # board 내에 있을 경우 new_coins에 위치 저장
                if board[nr][nc]=='#': # 움직일 위치가 벽이라면
                    new_coins.append((r,c)) # 원래 위치 고정
                    continue
                new_coins.append((nr,nc)) # 움직인 동전의 위치 저장
        if not new_coins: continue # 두 동전 다 떨어진 경우
        elif len(new_coins) == 1: # 한 동전이 떨어진 경우
            if ans > cnt+1: ans = cnt+1 # 현재 답보다 작을 경우 갱신
            return
        move(new_coins, cnt+1)

N,M = map(int,input().split())
board = [list(input()) for _ in range(N)]
coins = [] # 초기 동전의 위치 저장
for i in range(N):
    for j in range(M):
        if board[i][j]=='o':
            coins.append((i,j))
            board[i][j] = '.'
    if len(coins)==2: break
ans = 11
move(coins, 0)
print(-1 if ans==11 else ans)
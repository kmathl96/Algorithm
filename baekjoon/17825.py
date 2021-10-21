# 주사위 윷놀이
# 구현, 브루트포스, 백트래킹

def move(player,num):
    idx = loc[player] # player번째 말의 위치 좌표
    for _ in range(num): # num번 반복
        idx = nxt[idx] # 다음 칸으로 이동
        if idx==21: break # 도착 칸이면 종료
    if idx in blue.keys(): idx = blue[idx] # 파란색 칸에 도착하면 파란색 화살표 타기
    return idx # 도착한 위치 좌표 반환

def dfs(loc,d,score):
    global ans
    if d==10: # 10번 이동한 경우 종료
        if ans < score: ans = score # 점수가 현재 최대값보다 높은 경우 변경
        return
    
    # 말 이동
    for i in range(4):
        if loc[i] == 21: continue # 도착 칸에 있는 말은 움직이지 않음
        cur,nxt_idx = loc[i],move(i,nums[d]) # 해당 말의 현재 위치와 이동한 위치의 좌표
        if nxt_idx in loc and nxt_idx!=21: continue # 이동할 칸에 다른 말이 있는 경우 이동 못함 (도착 칸 예외)
        loc[i] = nxt_idx # 이동할 칸으로 위치 좌표 변경
        dfs(loc,d+1,score+board[nxt_idx]) # 다음 순서 진행
        loc[i] = cur # 원위치로 위치 좌표 변경

nums = list(map(int,input().split())) # 주사위에서 나올 수 10개
board = [2*i for i in range(21)]+[0,10,13,16,19]+[20,22,24]+[30,28,27,26,25,30,35] # 게임판의 값
nxt = [i+1 for i in range(len(board))] # 각 칸의 다음 칸 위치 좌표 : 바로 다음 칸으로 초기화
nxt[25],nxt[28],nxt[35] = 33,33,20 # 바로 다음 칸이 아닌 특정 칸으로 이동하는 칸
blue = {5:22,10:26,15:29} # 파란색 칸에 도착한 경우 이동할 위치 좌표
ans = 0 # 얻을 수 있는 점수의 최댓값
loc = [0,0,0,0] # 말의 위치 좌표
dfs(loc,0,0) # 현재 말들의 위치, 주사위 순서, 점수
print(ans)
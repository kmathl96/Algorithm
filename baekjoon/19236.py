# 청소년 상어
# 구현, 시뮬레이션, 백트래킹

from copy import deepcopy

board = [[0]*4 for _ in range(4)] # 공간

# 번호가 작은 물고기부터 이동
# 순서대로 처리하기 쉽게, 물고기의 정보를 따로 저장
info = [[0,0,0] for _ in range(17)] # info[i] = i번 물고기의 위치 좌표와 방향

dr,dc = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]
ans = 0 # 상어가 먹을 수 있는 물고기 번호의 합의 최댓값

# 물고기의 초기 정보 저장
for r in range(4):
    fish = list(map(int,input().split()))
    for c in range(4):
        num,d = fish[2*c],fish[2*c+1] # 번호와 방향
        board[r][c] = num
        info[num] = [r,c,d-1]

# 스택 : 공간과 물고기의 상태, 상어의 좌표와 방향, 상어가 먹은 물고기 번호의 합
st = [(board,info,0,0,0,board[0][0])]
while st:
    board,info,sr,sc,sd,cnt = st.pop()
    
    # 1. 상어가 물고기를 먹음
    eat = board[sr][sc] # 먹을 물고기의 번호
    board[sr][sc] = -1 # 상어의 위치는 -1로 표시
    sd = info[eat][2] # 상어의 방향은 먹은 물고기의 방향과 같아짐
    info[eat][2] = -1 # 먹힌 물고기는 방향을 -1로 변경하여 표시
    
    # 2. 물고기의 이동
    for i in range(1,17): # 번호가 작은 것부터
        r,c,d = info[i] # 위치 좌표와 방향
        if d==-1: continue # 이미 먹힌 물고기는 넘어감
        # 해당 방향부터 반시계 방향으로 45도씩 회전하며 탐색
        for j in range(8):
            nr,nc = r+dr[d],c+dc[d] # 이동할 위치
            # 유효한 위치이며, 빈 칸이거나 다른 물고기가 있는 경우 이동
            if 0<=nr<4 and 0<=nc<4 and board[nr][nc] >= 0:
                n1,n2 = board[r][c],board[nr][nc] # 이동할 물고기 번호
                info[n1],info[n2] = [nr,nc,d],[r,c,info[n2][2]] # 물고기 상태 변경
                board[r][c],board[nr][nc] = n2,n1 # 공간의 물고기 번호 변경
                break
            d = (d+1)%8 # 이동하지 못한 경우 다음 방향(45도 회전한 방향)으로 변경
    
    # 3. 상어의 이동
    isMoved = 0 # 상어 이동 여부
    nsr,nsc = sr,sc # 상어가 이동할 위치
    while True: # 한 칸씩 이동시키며 확인
        nsr,nsc = nsr+dr[sd],nsc+dc[sd] # 이동 방향으로 한 칸 이동
        if 0<=nsr<4 and 0<=nsc<4: # 유효한 위치인 경우
            num = board[nsr][nsc] # 이동할 위치에 있는 물고기의 번호
            if num > 0: # 물고기가 있는 칸만 이동 가능
                isMoved = 1
                board[sr][sc] = 0 # 상어가 있던 칸은 0으로 변경
                # 이동한 결과를 스택에 넣어 반복
                st.append((deepcopy(board),deepcopy(info),nsr,nsc,info[num][2],cnt+num))
                board[sr][sc] = -1 # 원상태로 변경
        else: break # 이동하지 못한 경우 종료
    if not isMoved and ans < cnt: ans = cnt # 이동할 수 없는 경우, ans와 비교하여 갱신
print(ans)
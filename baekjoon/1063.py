# 킹
# 구현, 시뮬레이션

king,stone,N = input().split() # 킹의 위치, 돌의 위치, 움직이는 횟수

# 킹과 돌의 위치를 좌표로 만들기
kr,kc,sr,sc = 8-int(king[1]),ord(king[0])-65,8-int(stone[1]),ord(stone[0])-65
dirs = {'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)} # 방향
cmds = [dirs[input()] for _ in range(int(N))] # 킹이 움직여야 하는 방향
for d in cmds:
    nkr,nkc = kr+d[0],kc+d[1] # 이동할 위치
    
    # 체스판 내의 위치인 경우 이동 (체스판 밖으로 나갈 경우에는 건너뜀)
    if 0<=nkr<8 and 0<=nkc<8:
        # 돌과 같은 곳인 경우, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동
        if sr==nkr and sc==nkc:
            nsr,nsc = sr+d[0],sc+d[1] # 돌이 이동할 위치

            # 체스판 내의 위치인 경우, 돌 이동
            if 0<=nsr<8 and 0<=nsc<8 : sr,sc = nsr,nsc
            # 돌이 체스판 밖으로 나갈 경우, 이동은 건너뜀
            else: continue
        kr,kc = nkr,nkc # 킹 이동

print(chr(kc+65)+str(8-kr)) # 킹의 마지막 위치
print(chr(sc+65)+str(8-sr)) # 돌의 마지막 위치
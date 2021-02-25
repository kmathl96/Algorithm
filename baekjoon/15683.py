# 감시
# 구현, 브루트포스, 시뮬레이션

from copy import deepcopy

def f(office,k,cnt): # 현재 사무실의 상태, 감시할 cctv, 감시 영역
    global mx
    if k==C: # 모든 cctv의 경우를 처리했으면 감시 영역 비교하여 갱신
        mx = max(mx,cnt)
        return
    r,c,d = cctv[k]
    for case in dirs[d]:
        tmp_cnt = 0
        tmp = deepcopy(office)
        for di in case:
            nr,nc=r,c
            while True:
                nr,nc = nr+di[0],nc+di[1]
                # 유효하지 않은 위치거나 벽을 만나면 멈춤
                if not (0<=nr<N and 0<=nc<M) or office[nr][nc]==6: break
                if not tmp[nr][nc]: tmp_cnt += 1
                tmp[nr][nc] = -1
        # 다음 cctv로 넘어감
        f(tmp,k+1,cnt+tmp_cnt)

N,M = map(int,input().split())
office = [list(map(int,input().split())) for _ in range(N)]

# 각 cctv의 가능한 감시 방법의 경우
dirs = [[],[[(0,1)],[(1,0)],[(0,-1)],[(-1,0)]],[[(0,1),(0,-1)],[(-1,0),(1,0)]],[[(-1,0),(0,1)],[(0,1),(1,0)],[(1,0),(0,-1)],[(0,-1),(-1,0)]],    [[(0,-1),(-1,0),(0,1)],[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)]],[[(-1,0),(0,1),(1,0),(0,-1)]]]

cnt0 = 0 # 0의 개수
cctv = [] # cctv의 위치와 종류
for r in range(N):
    for c in range(M):
        if not office[r][c]: cnt0 += 1
        elif 0<office[r][c]<6: cctv.append((r,c,office[r][c]))
C = len(cctv)
mx = 0 # 감시 영역의 수
f(office,0,0)
print(cnt0-mx)
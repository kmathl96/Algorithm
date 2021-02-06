# 로봇 청소기
# 구현, 시뮬레이션
# 탐색할 때 탐색 위치(nr,nc)가 유효한지(0<=nr<N and 0<=nc<M) 확인했었는데,
# 이 문제는 테두리가 전부 벽으로 되어있음을 전제로 하므로, 바로 탐색함 

D = [(-1,0),(0,1),(1,0),(0,-1)] # 북,동,남,서 (=> 시계 방향 순서)
def clean(r,c,d):
    global arr,ans
    
    if not arr[r][c]: # 1. 현재 위치를 청소
        arr[r][c] = 2
        ans += 1
    
    for i in range(4): # 2. 현재 위치에서 차례대로 탐색
        # 현재 방향 기준으로 왼쪽부터 탐색하며 청소를 못할 경우 그 자리에서 다시 왼쪽을 탐색
        # => 시계 반대 방향 순서
        # => 주어진 방향 리스트의 반대 순서로 탐색
        nd = (d-1-i)%4
        nr,nc = r+D[nd][0],c+D[nd][1]
        if not arr[nr][nc]: # 2-a. 청소하지 않은 공간
            clean(nr,nc,nd) # 그 방향으로 해당 위치 이동하여 반복
            return

    # 사방 탐색했지만 청소하지 못한 경우, 후진할 위치를 찾음
    # 원래 방향의 반대 방향으로 이동
    nd = (d+2)%4
    nr,nc = r+D[nd][0],c+D[nd][1]
    if arr[nr][nc]!=1: # 2-c. 해당 위치가 벽이 아닐 경우 청소 반복
        clean(nr,nc,d)

N,M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
clean(r,c,d)
print(ans)
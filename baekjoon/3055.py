# 탈출
# 그래프와 BFS

from collections import deque

R,C = map(int,input().split())
mp = [list(input()) for _ in range(R)]

# q에 물과 고슴도치의 위치를 저장
q = deque() # 위치 r,c와 걸린 시간 d를 넣을 것 (물은 d를 -1로)
for r in range(R):
    for c in range(C):
        if mp[r][c]=='S': start = (r,c,0) # 시작점 저장
        elif mp[r][c]=='*': q.append((r,c,-1))
q.append(start) # 물 먼저 퍼지므로 제일 마지막에 고슴도치의 시작점을 넣음

dr,dc = [-1,0,1,0],[0,1,0,-1]
ans = 0 # 비버의 굴로 이동할 수 있는지 여부를 판단하기 위해 0으로 초기화
while q:
    r,c,d = q.popleft()
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        # 탐색할 위치에 X, *이 있으면 물도 고슴도치도 가지 못하므로 아닌 경우만 고려
        if 0<=nr<R and 0<=nc<C and mp[nr][nc] not in 'X*':
            if d==-1: # 물인 경우
                if mp[nr][nc]!='D': # 비버의 굴이 아닌 경우
                    mp[nr][nc] = '*' # 물로 채움
                    q.append((nr,nc,-1))
            elif mp[nr][nc]=='D': # 비버의 굴로 도착
                ans = d+1
                break
            elif mp[nr][nc]=='.': # 비어있고 아직 방문하지 않은 곳
                mp[nr][nc] = 'v' # 중복으로 방문하지 않기 위함 (visited)
                q.append((nr,nc,d+1))
    if ans: break # ans 값이 0에서 바뀌었다면, 최솟값을 찾은 것임
print(ans if ans else 'KAKTUS')
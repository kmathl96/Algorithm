# 인구 이동
# 구현, 그래프 탐색, 시뮬레이션

dr,dc = [-1,0,1,0],[0,1,0,-1]
def move(r,c):
    visited[r][c] = 1
    st = [(r,c)]
    connected = [(r,c)]
    sum_p = pop[r][c]
    while st:
        r,c = st.pop()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and L <= abs(pop[r][c]-pop[nr][nc]) <= R:
                st.append((nr,nc))
                connected.append((nr,nc))
                sum_p += pop[nr][nc]
                visited[nr][nc] = 1
    # 연결된 나라가 없을 경우 0 반환
    if len(connected) == 1: return 0
    # 연결된 나라들의 인구 수를 평균 인구 수로 저장
    avg = sum_p//len(connected)
    for r,c in connected:
        pop[r][c] = avg
    return 1

def check(pop):
    global visited
    visited = [[0]*N for _ in range(N)]
    flag = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            visited[r][c] = 1
            if move(r,c) and not flag: flag = 1
    return flag

N,L,R = map(int,input().split())
pop = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
while True:
    if not check(pop): break
    cnt += 1
print(cnt)
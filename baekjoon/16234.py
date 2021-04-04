# 인구 이동
# 구현, 그래프 탐색, 시뮬레이션

# 매번 모든 나라를 탐색하지 말고,
# 이전 차례에서 연합을 구성했었던 나라들만 탐색해야
# 시간을 단축시킬 수 있음 (7xxx ms => 4xx ms)

from collections import deque

dr,dc = [-1,0,1,0],[0,1,0,-1]
def move(r,c):
    visited[r][c] = 1
    st = [(r,c)]
    conn = [(r,c)] # 연합
    sum_p = pop[r][c]
    while st:
        r,c = st.pop()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and L <= abs(pop[r][c]-pop[nr][nc]) <= R:
                st.append((nr,nc))
                conn.append((nr,nc)) # 연합에 추가
                sum_p += pop[nr][nc]
                visited[nr][nc] = 1
    # 연결된 나라가 없을 경우 0 반환
    if len(conn) == 1: return 0
    # 연합국의 인구 수를 평균 인구 수로 저장
    avg = sum_p//len(conn) # 평균 인구 수
    for r,c in conn:
        pop[r][c] = avg
        group.append((r,c)) # 다음에 탐색할 나라 추가
    return 1

N,L,R = map(int,input().split())
pop = [list(map(int,input().split())) for _ in range(N)]
cnt = -1
group = deque([(r,c) for c in range(N) for r in range(N)]) # 탐색할 나라
flag = 1 # 인구 이동 여부
while flag: # 인구 이동이 안 일어날 경우 종료
    visited = [[0]*N for _ in range(N)]
    flag = 0
    for _ in range(len(group)):
        r,c = group.popleft()
        # 방문하지 않았을 경우 탐색하여, 인구 이동 발생 시 flag 갱신
        if not visited[r][c] and move(r,c): flag = 1
    cnt += 1
print(cnt)
# 원판 돌리기
# 구현, 시뮬레이션

from collections import deque

dr,dc = [-1,0,1,0],[0,1,0,-1]

# (r,c)와 인접하면서 같은 값을 갖는 칸을 찾고, 그러한 수가 있는 경우 그 값을 지움
def dfs(r,c,val):
    st = [(r,c)]
    remove_nums = [(r,c)] # (r,c)와 인접하면서 같은 값을 가지고 있는 칸 => 지우기
    flag = 0 # 인접하면서 수가 같은 칸이 있는지 여부
    while st:
        r,c = st.pop()
        visited[r][c] = 1
        for i in range(4):
            # 첫 열과 끝 열이 인접하므로 % 연산으로 처리
            nr,nc = r+dr[i],(c+dc[i])%M
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and val==nums[nr][nc]:
                st.append((nr,nc))
                remove_nums.append((nr,nc))
                flag = 1
    
    # 인접하면서 수가 같은 칸이 없는 경우, 0 반환
    if not flag: return 0
    # 있는 경우, 해당하는 칸의 값을 지우고 1 반환
    for r,c in remove_nums:
        nums[r][c] = 0
    return 1

# 원판의 반지름 크기, 원판에 적힌 정수의 개수, 원판을 회전시킬 횟수
N,M,T = map(int,input().split())
nums = [deque(map(int,input().split())) for _ in range(N)] # 원판에 적힌 수
for _ in range(T):
    # 번호가 x의 배수인 원판을 d 방향으로 k칸 회전
    x,d,k = map(int,input().split())
    for r in range(x-1,N,x):
        nums[r].rotate(-k if d else k)
    
    visited = [[0]*M for _ in range(N)] # 확인했는지 여부
    removed = 0 # 인접하면서 수가 같은 칸이 있는지 여부
    for r in range(N):
        for c in range(M):
            # 수가 있고, 인접하면서 같은 값을 갖는 칸이 있는 경우 removed를 1로 변경
            if nums[r][c] and dfs(r,c,nums[r][c]): removed = 1
    if removed: continue
    # 없는 경우,
    # 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수는 1 감소, 작은 수는 1 증가
    cnt,sum_ = 0,0 # 원판에 남아있는 수의 개수와 합
    for r in range(N):
        for c in range(M):
            if nums[r][c]:
                cnt += 1
                sum_ += nums[r][c]
    if not cnt: break # 남아있는 수가 없다면 종료
    avg = sum_/cnt # 평균
    for r in range(N):
        for c in range(M):
            if not nums[r][c]: continue
            if nums[r][c] > avg: nums[r][c] -= 1 # 평균보다 큰 수는 1 빼기
            elif nums[r][c] < avg: nums[r][c] += 1 # 평균보다 작은 수는 1 더하기
print(sum(sum(row) for row in nums)) # 원판에 적힌 수의 합
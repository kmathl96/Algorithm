# 원판 돌리기
# 구현, 시뮬레이션

# 원판의 반지름 크기, 원판에 적힌 정수의 개수, 원판을 회전시킬 횟수
N,M,T = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(N)] # 원판에 적힌 수

# 원판에 적힌 수의 개수와 합 구하기
cnt,sum_ = 0,0
for r in range(N):
    for c in range(M):
        if nums[r][c]:
            cnt += 1
            sum_ += nums[r][c]

# T번 회전
for _ in range(T):
    # 번호가 x의 배수인 원판을 d 방향으로 k칸 회전
    x,d,k = map(int,input().split())

    # 1. 회전
    # 반시계 방향인 경우, 처음~k칸를 뒤에 붙임
    # 시계 방향인 경우, (M-k)~끝칸을 앞에 붙임
    if not d: k = M-k
    for r in range(x-1,N,x):
        nums[r] = nums[r][k:]+nums[r][:k]
    
    # 2-1. 인접하면서 수가 같은 것 지우기
    remove = set()
    for r in range(N):
        for c in range(M):
            if not nums[r][c]: continue # 0이면 넘어감
            # 다음 열(c=M인 경우, 처음 열)과 같은 값인 경우, 두 좌표 넣기
            if nums[r][c] == nums[r][(c+1)%M]:
                remove.add((r,c))
                remove.add((r,(c+1)%M))
            # 다음 행과 같은 값인 경우, 두 좌표 넣기
            if r<N-1 and nums[r][c] == nums[r+1][c]:
                remove.add((r,c))
                remove.add((r+1,c))
    for r,c in remove:
        sum_ -= nums[r][c]
        cnt -= 1
        nums[r][c] = 0
    
    if not cnt: break # 남아있는 수가 없다면 종료
    if remove: continue

    # 2-2. 인접하면서 수가 같은 것이 없는 경우
    avg = sum_/cnt # 평균
    for r in range(N):
        for c in range(M):
            if nums[r][c] > avg:
                sum_ -= 1 # 합 갱신
                nums[r][c] -= 1 # 평균보다 큰 수는 1 빼기
                # 해당 칸의 값이 0이 되면 원판에 있는 수의 개수 갱신
                if not nums[r][c]: cnt -= 1
            elif 0 < nums[r][c] < avg:
                sum_ += 1 # 합 갱신
                nums[r][c] += 1 # 평균보다 작은 수는 1 더하기
print(sum_) # 합 출력


### 큐와 DFS를 활용한 풀이 (실행 속도 2배 정도 느림) ###
# from collections import deque

# dr,dc = [-1,0,1,0],[0,1,0,-1]

# # (r,c)와 인접하면서 같은 값을 갖는 칸을 찾고, 그러한 수가 있는 경우 그 값을 지움
# def dfs(r,c,val):
#     st = [(r,c)]
#     remove_nums = [(r,c)] # (r,c)와 인접하면서 같은 값을 가지고 있는 칸 => 지우기
#     flag = 0 # 인접하면서 수가 같은 칸이 있는지 여부
#     while st:
#         r,c = st.pop()
#         visited[r][c] = 1
#         for i in range(4):
#             # 첫 열과 끝 열이 인접하므로 % 연산으로 처리
#             nr,nc = r+dr[i],(c+dc[i])%M
#             if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and val==nums[nr][nc]:
#                 st.append((nr,nc))
#                 remove_nums.append((nr,nc))
#                 flag = 1

#     # 인접하면서 수가 같은 칸이 없는 경우, 0 반환
#     if not flag: return 0
#     # 있는 경우, 해당하는 칸의 값을 지우고 1 반환
#     for r,c in remove_nums:
#         nums[r][c] = 0
#     return 1

# # 원판의 반지름 크기, 원판에 적힌 정수의 개수, 원판을 회전시킬 횟수
# N,M,T = map(int,input().split())
# nums = [deque(map(int,input().split())) for _ in range(N)] # 원판에 적힌 수
# for _ in range(T):
#     # 번호가 x의 배수인 원판을 d 방향으로 k칸 회전
#     x,d,k = map(int,input().split())
#     for r in range(x-1,N,x):
#         nums[r].rotate(-k if d else k)

#     visited = [[0]*M for _ in range(N)] # 확인했는지 여부
#     removed = 0 # 인접하면서 수가 같은 칸이 있는지 여부
#     for r in range(N):
#         for c in range(M):
#             # 수가 있고, 인접하면서 같은 값을 갖는 칸이 있는 경우 removed를 1로 변경
#             if nums[r][c] and dfs(r,c,nums[r][c]): removed = 1
#     if removed: continue
#     # 없는 경우,
#     # 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수는 1 감소, 작은 수는 1 증가
#     cnt,sum_ = 0,0 # 원판에 남아있는 수의 개수와 합
#     for r in range(N):
#         for c in range(M):
#             if nums[r][c]:
#                 cnt += 1
#                 sum_ += nums[r][c]
#     if not cnt: break # 남아있는 수가 없다면 종료
#     avg = sum_/cnt # 평균
#     for r in range(N):
#         for c in range(M):
#             if not nums[r][c]: continue
#             if nums[r][c] > avg: nums[r][c] -= 1 # 평균보다 큰 수는 1 빼기
#             elif nums[r][c] < avg: nums[r][c] += 1 # 평균보다 작은 수는 1 더하기
# print(sum(sum(row) for row in nums)) # 원판에 적힌 수의 합 
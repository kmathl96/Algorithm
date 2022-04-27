# 숫자판 점프
# 브루트포스, DFS

def dfs(r,c,s):
    # 현재 수의 길이가 5인 경우, 종료
    if len(s)==6:
        nums.add(s) # set에 넣기
        return
    
    # 인접한 칸 탐색
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i] # 이동할 위치
        if 0<=nr<5 and 0<=nc<5:
            # 해당 위치에 적힌 숫자를 붙인 후, 더 탐색
            dfs(nr,nc,s+board[nr][nc])

board = [input().split() for _ in range(5)] # 숫자판
nums = set() # 만들 수 있는 수들
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
for r in range(5):
    for c in range(5):
        # (r,c) 위치에서 시작하여 여섯 자리의 수 만들기
        dfs(r,c,board[r][c])

# 만들 수 있는 수들의 개수 출력
print(len(nums))
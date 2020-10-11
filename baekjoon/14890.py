# Baekjoon 14890. 경사로

def r_check(r,c,v):
    global r_visistd
    if r < -1 or c < -1 or c + L >= N: return 1
    for i in range(L):
        if arr[r][c+1+i] != v or r_visited[c+1+i]:
            return 1
    for i in range(L):
        r_visited[c+1+i] = 1
    return 0

def c_check(r,c,v):
    global c_visited
    if r < -1 or c < -1 or r + L >= N: return 1
    for i in range(L):
        if arr[r+1+i][c] != v or c_visited[r+1+i]:
            return 1
    for i in range(L):
        c_visited[r+1+i] = 1
    return 0

N,L = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
r_ans = [1]*N
c_ans = [1]*N

for r in range(N):
    r_visited = [0]*N
    for c in range(N-1):
        if r_ans[r]:
            diff = arr[r][c+1] - arr[r][c]
            if abs(diff) > 1: r_ans[r] = 0
            elif diff == -1 and r_check(r,c,arr[r][c+1]):
                r_ans[r] = 0
            elif diff == 1 and r_check(r,c-L,arr[r][c]):
                r_ans[r] = 0

for c in range(N):
    c_visited = [0]*N
    for r in range(N-1):      
        if c_ans[c]:
            diff = arr[r+1][c] - arr[r][c]
            if abs(diff) > 1: c_ans[c] = 0
            elif diff == -1 and c_check(r,c,arr[r+1][c]):
                c_ans[c] = 0
            elif diff == 1 and c_check(r-L,c,arr[r][c]):
                c_ans[c] = 0
print(sum(r_ans)+sum(c_ans))
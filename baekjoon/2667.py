# 단지번호붙이기
# 그래프와 BFS

dr,dc = [-1,0,1,0],[0,1,0,-1]
def dfs(row,col):
    global arr
    cnt = 1 # 이 단지에 속하는 집의 수, 시작점을 포함하므로 1
    arr[row][col] = '0'
    st = [(row,col)]
    while st:
        r,c = st.pop()
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc]=='0': continue
                arr[nr][nc] = '0' # 더 탐색하지 않도록 값 바꿔줌
                st.append((nr,nc)) # 해당 위치에서 더 탐색하기 위해 스택에 넣음
                cnt += 1
    return cnt

N = int(input())
arr = [list(input()) for _ in range(N)]
ans = [] # 각 단지에 속하는 집의 수
for i in range(N):
    for j in range(N):
        if arr[i][j]=='1': ans.append(dfs(i,j))
print(len(ans)) # 단지 수
for i in sorted(ans):
    print(i)
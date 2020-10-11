# 2. 물난리

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def f(n, isEnd):
  for i in range(N):
    for j in range(N):
      if arr[i][j]==n:
        for k in range(4):
          nr,nc = i+dr[k],j+dc[k]
          if 0<=nr<N and 0<=nc<N:
            if arr[nr][nc]==-1:
              isEnd = True
              break
            if arr[nr][nc]==0: arr[nr][nc] = n+1
      if isEnd: break
    if isEnd: break

def g():
  for i in range(N):
    for j in range(N):
      if arr[i][j]==-1:
        for k in range(4):
          nr,nc = i+dr[k],j+dc[k]
          if 0<=nr<N and 0<=nc<N and arr[nr][nc]==0:
            arr[nr][nc] = -1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr[0][0] = 2
arr[N-1][N-1] = -1
t = 2
# f(t, isEnd)
isEnd = False
while not isEnd:
  t+=1
  f(t, isEnd)
  g()

for row in arr:
  print(row)
print(sum(row.count(0)+row.count(-1) for row in arr)-1)
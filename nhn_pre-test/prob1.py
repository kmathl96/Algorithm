N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]
ans1 = 0
ans2 = []
for r in range(N):
  for c in range(N):
    if arr[r][c]:
      st = [(r,c)]
      arr[r][c] = 0
      ans1 += 1
      cnt = 0
      while st:
        r,c = st.pop()
        cnt += 1
        for i in range(4):
          nr,nc = r+dr[i],c+dc[i]
          if 0<=nr<N and 0<=nc<N and arr[nr][nc]:
            arr[nr][nc] = 0
            st.append((nr,nc))
      ans2.append(cnt)
print(f'{ans1}\n{" ".join(map(str, sorted(ans2)))}')
# Baekjoon 17406. 배열 돌리기 4

import copy

def rotate(lst,r,c,s):
  arr = copy.deepcopy(lst)
  for j in range(s):
    for i in range(r-s-1+j,r+s-1-j):
      a = arr[i].pop(c-1+s-j)
      arr[i].insert(c-1-s+j,arr[i+1].pop(c-1-s+j))
      arr[i+1].insert(c-1+s-j-1,a)
    arr[r-1+s-j].insert(c-1+s-1-j,arr[r-1+s-j].pop(c+s-1-j))
  return arr

def f(arr, d, v):
  global ans
  if d == K:
    tmp = min(list(sum(row) for row in arr))
    if ans > tmp: ans = tmp
    return
  for i in range(K):
    if not v[i]:
      v[i] = 1
      arr2 = rotate(arr,rot[i][0],rot[i][1],rot[i][2])
      f(arr2, d+1, v)
      v[i] = 0

N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
rot = [list(map(int,input().split())) for _ in range(K)]
ans = 5000
visited = [0]*K
f(A,0,visited)
print(ans)
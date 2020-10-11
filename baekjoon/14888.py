# Baekjoon 14888. 연산자 끼워넣기

def f(ops, val, k):
  global mx,mn
  if k==N:
    if mx < val: mx = val
    if mn > val: mn = val
    return
  
  for i in range(4):
    if ops[i]==0: continue
    ops[i]-=1
    if i==0: f(ops, val+A[k], k+1)
    elif i==1: f(ops, val-A[k], k+1)
    elif i==2: f(ops, val*A[k], k+1)
    elif i==3: f(ops, val//A[k] if val>=0 else -(-val//A[k]), k+1)
    ops[i]+=1

N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))
mx,mn = -1000000000, 1000000000
f(ops, A[0], 1)
print(f'{mx}\n{mn}')
# 연산자 끼워넣기 (2)
# 브루트 포스

def f(cur,val):
    global mx,mn,ops
    if cur == N:
        # 최대값, 최소값 갱신
        if mx < val: mx = val
        if mn > val: mn = val
        return
    for i in range(4): # 사칙연산 수행
        if not ops[i]: continue
        ops[i] -= 1 # 연산 횟수 감소
        # 연산 횟수가 남은 경우 수행
        if i==0: f(cur+1, val+A[cur])
        elif i==1: f(cur+1, val-A[cur])
        elif i==2: f(cur+1, val*A[cur])
        else: f(cur+1, -(-val//A[cur]) if val < 0 else val//A[cur])
        ops[i] += 1 # 연산 횟수 되돌리기
    
N = int(input())
A = list(map(int,input().split()))
ops = list(map(int,input().split())) # 각 연산의 횟수
mn = 10**9
mx = -mn
f(1,A[0])
print(mx)
print(mn)
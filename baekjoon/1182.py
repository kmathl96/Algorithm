# 부분수열의 합
# 브루트 포스

def f(cur,val):
    global ans
    if cur == N:
        if val == S: ans += 1
        return
    f(cur+1,val+num[cur])
    f(cur+1,val)

N,S = map(int,input().split())
num = list(map(int,input().split()))
ans = 0
f(0,0)
if S==0: ans -= 1 # S=0일 때, 아무 것도 더하지 않는 경우가 있으므로 -1
print(ans)
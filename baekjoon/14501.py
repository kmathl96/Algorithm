# Baekjoon 14501. 퇴사

def f(k, sum_p):
    global ans
    for i in range(k+1,N+1):
        nxt = i-1+arr[i-1][0]
        if nxt <= N:
            f(nxt, sum_p+arr[i-1][1])
    if sum_p > ans: ans = sum_p
   
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
f(0,0)
print(ans)
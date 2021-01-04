# 1, 2, 3 더하기
# 기초 - 브루트 포스

def f(n,val):
    global ans
    if val==n: ans += 1
    for i in range(1,min(4,n-val+1)):
        f(n,val+i)

for _ in range(int(input())):
    ans = 0
    f(int(input()),0)
    print(ans)
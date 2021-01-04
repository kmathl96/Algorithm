# 이전 순열
# 기초 - 브루트 포스

N = int(input())
num = list(map(int,input().split()))
tmp = num.index(1)
for i in range(N-2,-1,-1):
    if num[i] < num[i+1]: continue
    for j in range(i+1,N):
        if num[tmp] < num[j] < num[i]: tmp = j
    num[tmp],num[i] = num[i],num[tmp]
    break
print(" ".join(map(str,num[:i+1]+sorted(num[i+1:], reverse=1))) if tmp else -1)
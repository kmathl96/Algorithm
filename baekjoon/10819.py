# 차이를 최대로
# 기초 - 브루트 포스

from itertools import permutations

N = int(input())
num = list(map(int,input().split()))
ans = 0
for case in permutations(num,N): # 조합
    tmp = 0
    for i in range(N-1):
        tmp += abs(case[i]-case[i+1])
    if ans < tmp: ans = tmp # 최대값 갱신
print(ans)
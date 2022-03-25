# 구간 합 구하기 4
# 누적 합

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 수의 개수, 합을 구해야 하는 횟수
nums = [0]+list(map(int,input().split())) # N개의 수
for i in range(1,N+1):
    nums[i] += nums[i-1] # 1번째 수부터 i번째 수까지의 누적 합 저장

# 합 구하기
ans = []
for _ in range(M):
    # [i~j]의 합은 [1~j]의 합에서 [1~(i-1)]의 합을 뺀 값과 같음
    i,j = map(int,input().split()) # 구간 i와 j
    ans.append(nums[j]-nums[i-1])

print('\n'.join(map(str,ans)))
# Baekjoon 11053. 가장 긴 증가하는 부분 수열
# 다이나믹 프로그래밍

N = int(input())
A = list(map(int,input().split()))
dp = [1]*N # 본인만 부분 수열을 구성할 경우 그 길이가 1이므로 1로 초기화

for i in range(1,N):
    for j in range(i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
print(max(dp))
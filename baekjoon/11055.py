# 가장 큰 증가 부분 수열
# 다이나믹 프로그래밍

N = int(input())
A = list(map(int,input().split()))
dp = A[:] # 자신으로만 구성된 부분 수열의 합(=자신의 값)으로 초기화
for i in range(N):
    for j in range(i):
        # 증가 수열일 경우
        # 앞 값의 부분 수열에 자신을 추가한 경우의 크기 합과 현재 자신의 부분 수열의 크기 합 비교
        if A[j] < A[i] and dp[j]+A[i] > dp[i]:
            dp[i] = dp[j]+A[i]
print(max(dp))
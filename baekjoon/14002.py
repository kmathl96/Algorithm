# 가장 긴 증가하는 부분 수열 4
# 다이나믹 프로그래밍

N = int(input())
A = list(map(int,input().split()))
# 부분 수열 저장
# 자신으로만 구성된 부분 수열로 초기화
dp = [[A[i]] for i in range(N)]
for i in range(N):
    for j in range(i):
        # 이전 값(A[j])이 자신 값보다 작고 (= 증가 수열)
        # 이전의 부분 수열(dp[j])에 자기를 추가(+1)한 수열이 현재 자기의 부분 수열(dp[i])보다 큰 경우
        if A[j] < A[i] and len(dp[j])+1 > len(dp[i]):
            dp[i] = dp[j] + [A[i]] # 자신의 부분 수열을 이전의 부분 수열에 자기를 추가한 수열로 변경
dp.sort(key=lambda x: len(x)) # 부분 수열의 길이순으로 정렬
print(len(dp[-1]))
print(*dp[-1])

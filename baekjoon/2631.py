# 줄세우기
# 다이나믹 프로그래밍

N = int(input()) # 아이들의 수
nums = [int(input()) for _ in range(N)] # 아이들이 서 있는 순서
dp = [1]*N

# 번호 순서대로 서있는 가장 긴 부분 수열 찾기
for i in range(1,N):
    # 앞에 서있는 아이들의 경우와 비교
    for j in range(i):
        # 해당 아이(j)보다 번호가 큰 경우, 제대로 서있는 것임
        if nums[i] > nums[j]:
            # 저장된 값(dp[i])과 해당 아이의 뒤에 서는 경우의 값(dp[j]+1) 비교
            dp[i] = max(dp[i],dp[j]+1)

# 순서대로 서있지 않은 아이들만 옮기면 됨
# N명 중에서 순서대로 서있는 아이들의 수의 최댓값을 뺌
print(N-max(dp))
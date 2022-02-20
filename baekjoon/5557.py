# 1학년
# DP

N = int(input()) # 숫자의 개수
nums = list(map(int,input().split())) # 숫자들

# dp[i][j] = i번째 숫자를 더하거나 빼서 j를 만들 수 있는 등식의 개수
dp = [[0]*21 for _ in range(N-1)]
dp[0][nums[0]] = 1 # 맨 앞 숫자는 초기화

# 숫자 순서대로 경우의 수를 계산
for i in range(1,N-1):
    num = nums[i] # 계산할 숫자

    # 이전 결과에 더하거나 빼기
    for j in range(21):
        if dp[i-1][j]:
            # 상근이는 0~20만 알기 때문에 계산값이 범위 내에 있는 경우만 고려
            # 1. 더하기
            if j+num<=20:
                dp[i][j+num] += dp[i-1][j]
            # 2. 빼기
            if j-num>=0:
                dp[i][j-num] += dp[i-1][j]

# 숫자들 중 마지막에서 2번째 숫자까지 계산한 결과 중
# 마지막 숫자와 같은 값인 경우의 등식 개수 출력
print(dp[N-2][nums[-1]])
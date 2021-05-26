# 2×n 타일링 2
# 다이나믹 프로그래밍
# 11726. 2×n 타일링과 같은 방식

n = int(input())
dp = [1]*(n+1)
for i in range(2,n+1):
    # 1. 2×(i-1)의 크기의 직사각형에, 2×1 타일을 붙여 2×i 크기의 직사각형을 만들 수 있음 => dp[i-1]
    # 2. 2×(i-2)의 크기의 직사각형에, 1×2 타일 2개를 붙이거나 2×2 타일을 붙여 2×i 크기의 직사각형을 만들 수 있음 => dp[i-2]*2
    # 2×i의 크기의 직사각형을 만들 수 있는 경우의 수는 위의 두 가지 경우의 수를 더한 값임
    dp[i] = dp[i-1]+dp[i-2]*2
print(dp[n]%10007)
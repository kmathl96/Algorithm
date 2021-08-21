# 1, 2, 3 더하기 4
# 다이나믹 프로그래밍

T = int(input()) # 테스트 케이스의 개수
nums = [int(input()) for _ in range(T)] # 정수

# 1부터 10000(n의 최댓값)까지의 답을 미리 계산해놓음
dp = [0]*(10001) # dp[i] = 1, 2, 3의 합으로 i를 나타내는 방법의 수
dp[0] = 1
for i in range(1,4):
    for j in range(i,10001):
        dp[j] += dp[j-i] # i만큼 작은 수를 만드는 방법의 수 만큼 더하기

# 각 테스트 케이스마다 n 1, 2, 3의 합으로 나타내는 방법의 수 출력
for n in nums:
    print(dp[n])
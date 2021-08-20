# 동전 1
# 다이나믹 프로그래밍

n,k = map(int,input().split()) # 동전의 종류 수, 동전으로 만들 가치의 합
coins = [int(input()) for _ in range(n)] # 동전의 가치
dp = [0]*(k+1) # dp[i] = i원을 만들 수 있는 경우의 수
dp[0] = 1

for val in coins:
    # 동전을 더해서 i원 만들기
    for i in range(val,k+1): # 해당 동전의 가치부터 시작
        # 해당 동전의 가치만큼 적은 금액(i-val)을 만들 수 있는 경우의 수를 더함
        dp[i] += dp[i-val]
print(dp[k])
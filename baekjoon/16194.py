# 카드 구매하기 2
# 다이나믹 프로그래밍
# 11052. 카드 구매하기와 동일한 방법

N = int(input())
P = [0] + list(map(int,input().split()))
dp = [10000]*(N+1) # dp의 값들을 입력 최댓값인 10000으로 초기화
for i in range(1,N+1):
    dp[i] = min(P[i],min([P[j]+dp[i-j] for j in range(i//2+1)]))
print(dp[-1])
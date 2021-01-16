# 카드 구매하기
# 다이나믹 프로그래밍

N = int(input())
P = [0] + list(map(int,input().split()))
dp = [0]*(N+1) # 각 장별로 최대 금액을 저장할 리스트
for i in range(1,N+1): # i장 살 때 최대 금액 구하기
    # i//2+1보다 작은 모든 j의 "i-j장 살 때 최대 금액 + j장 들어있는 팩 가격" 중 최댓값과
    # i장 들어있는 팩 중 더 비싼 금액 찾음
    dp[i] = max(P[i],max([P[j]+dp[i-j] for j in range(i//2+1)]))
print(dp[-1]) # 마지막 값(N장 살 때 최대 금액) 출력
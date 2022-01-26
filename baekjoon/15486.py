# 퇴사 2
# DP

import sys
input = sys.stdin.readline

N = int(input()) # 퇴사 전까지 남은 일수
schedule = [list(map(int,input().split())) for _ in range(N)] # 상담 일정표
dp = [0]*(N+1) # dp[i] = i일째까지 일할 때 받을 수 있는 금액의 최댓값

for i in range(N):
    T,P = schedule[i] # 상담을 완료하는 데 걸리는 기간, 상담을 했을 때 받을 수 있는 금액
    
    # 이전 날의 누적 금액이 더 큰 경우 변경
    if dp[i] > dp[i+1]: dp[i+1] = dp[i]
    
    # 상담을 했을 때의 누적액이 T일 후 누적액보다 큰 경우 변경
    if i+T<=N and dp[i]+P > dp[i+T]: dp[i+T] = dp[i]+P

print(dp[-1]) # 마지막 날의 값 출력
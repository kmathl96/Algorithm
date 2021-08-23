# 평범한 배낭
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N,K = map(int,input().split()) # 물건의 개수, 들 수 있는 최대 무게

# dp[r][c] = r번째 물건을 고려했을 때, c만큼의 무게를 드는 경우 즐길 수 있는 최대 가치
dp = [[0]*(K+1) for _ in range(N+1)]

for idx in range(1,N+1):
    W,V = map(int,input().split()) # idx번째 물건의 무게와 가치
    
    # 각 무게만큼 들 수 있는 물건 가치 합의 최댓값 구하기
    for weight in range(1,K+1):
        # 물건이 더 무겁다면, 배낭에 넣을 수 없음
        # 해당 물건을 안 넣은 그 무게의 가치를 저장
        if weight < W: dp[idx][weight] = dp[idx-1][weight]
        
        # 배낭에 넣을 수 있다면,
        # 1. 물건을 넣는 경우(해당 물건의 무게만큼 적은 경우의 가치+해당 물건의 가치)
        # 2. 물건을 안 넣는 경우(해당 물건을 넣지 않은 그 무게의 가치)
        # 중에서 가치가 더 큰 것을 저장
        else: dp[idx][weight] = max(dp[idx-1][weight-W]+V,dp[idx-1][weight])

# N번째 물건까지 고려했을 때 K만큼의 무게를 드는 경우들 중, 최대의 가치 출력
print(dp[N][K])
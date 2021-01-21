# 연속합
# 다이나믹 프로그래밍

n = int(input())
num = list(map(int,input().split()))
dp = [0]*n # 각각의 수를 선택하는 경우들 중 최댓값
for i in range(n):
    # 앞의 연속합(dp[i-1])에 i번째 수(num[i])를 더했을 때의 값 비교
    # i번째 수보다 작다면, i번째 수를 연속합의 시작점으로 두고 num[i]를 저장
    # i번째 수보다 크다면, i번째 수를 연속합에 더함
    dp[i] = max(num[i], dp[i-1]+num[i])
print(max(dp))
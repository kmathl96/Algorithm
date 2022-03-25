# 공통 부분 문자열
# 다이나믹 프로그래밍, 문자열

s1,s2 = input(),input() # 두 문자열
N,M = len(s1),len(s2) # 각 문자열의 길이
dp = [[0]*(M+1) for _ in range(N+1)]

ans = 0 # 두 문자열에 모두 포함된 부분 문자열 중 가장 긴 것의 길이
for i in range(1,N+1):
    for j in range(1,M+1):
        # s1의 (i-1)번째 글자와 s2의 (j-1)번째 글자가 같은 경우
        # 해당 글자를 부분 문자열에 포함시킴
        if s1[i-1]==s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1 # (이전의 부분 문자열의 길이+1) 저장
            ans = max(ans,dp[i][j]) # 답 갱신
print(ans)
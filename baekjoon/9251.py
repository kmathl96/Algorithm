# LCS
# 다이나믹 프로그래밍

str1,str2 = input(),input() # 두 문자열

# dp[i][j] = str2의 i번째까지, str1의 j번째까지의 LCS의 길이
dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]

for i in range(len(str2)):
    for j in range(len(str1)):
        # 같은 문자인 경우
        if str2[i]==str1[j]:
            # 해당 문자를 포함하지 않은 경우의 LCS 길이 + 1
            dp[i+1][j+1] = dp[i][j]+1
        # 다른 문자인 경우
        else:
            # 해당 문자를 포함하지 않는 LCS 중 더 긴 값
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
print(dp[-1][-1])
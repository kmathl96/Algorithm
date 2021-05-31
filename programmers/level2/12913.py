# 땅따먹기

def solution(land):
    answer = [0,0,0,0] # 해당 열을 밟을 때 최대 점수
    for l in land:
        dp = answer[:]
        # 해당 열을 제외한 칸 중에서 최대 점수 + 해당 열의 점수
        answer[0] = max(dp[1],dp[2],dp[3]) + l[0]
        answer[1] = max(dp[0],dp[2],dp[3]) + l[1]
        answer[2] = max(dp[0],dp[1],dp[3]) + l[2]
        answer[3] = max(dp[0],dp[1],dp[2]) + l[3]
    return max(answer) # 그 중에서 제일 큰 값 반환

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])) # 16

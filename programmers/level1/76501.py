# 음양 더하기
# 월간 코드 챌린지 시즌2

def solution(absolutes, signs):
    # signs[i]가 True이면 1, False이면 -1을 absolutes[i]에 곱하여 그 값들의 합을 반환
    return sum([absolutes[i]*(1 if signs[i] else -1) for i in range(len(signs))])

print(solution([4,7,12], [True,False,True])) # 9
print(solution([1,2,3], [False,False,True])) # 0
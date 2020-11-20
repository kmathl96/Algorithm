# 자릿수 더하기

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

print(solution(123)) # 6
print(solution(987)) # 24
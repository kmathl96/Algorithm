# 하샤드 수

def solution(x):
    # 각 자릿수의 합으로 x를 나눠지면 0(=false)이고 not으로 true로 바꿈
    # 마찬가지로, 나눠지지 않는 경우는 false로 반환
    return not x%sum(map(int,str(x)))

print(solution(10)) # true
print(solution(12)) # true
print(solution(11)) # false
print(solution(13)) # false
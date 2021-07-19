# 약수의 개수와 덧셈
# 월간 코드 챌린지 시즌2

def solution(left, right):
    # 약수의 개수가 홀수 => 소수
    # 제곱근을 내림한 값을 다시 제곱했을 때 해당 값이 나오는지를 확인하여 소수 판단
    # 소수라면 음수로, 아니라면 양수 그대로 총합 반환
    return sum(-num if int(num**0.5)**2==num else num for num in range(left,right+1))

print(solution(13, 17)) # 43
print(solution(24, 27)) # 52
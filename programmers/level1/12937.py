# 짝수와 홀수

def solution(num):
    # 1과 & 연산(각 자리에서 둘 다 1일 때 1임) 했을 때
    # 1이면 홀수, 0이면 짝수
    return 'Odd' if num&1 else 'Even'

print(solution(3)) # "Odd"
print(solution(4)) # "Even"

print(solution(0)) # "Even"
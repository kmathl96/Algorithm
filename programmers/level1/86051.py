# 없는 숫자 더하기

def solution(numbers):
    return 45-sum(numbers) # 0~9의 합에서 numbers의 숫자들의 합을 뺌

print(solution([1,2,3,4,6,7,8,0])) # 14
print(solution([5,8,4,0,6,7,9])) # 6
# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for a in arr:
        if not a%divisor: answer.append(a)
    return sorted(answer) if answer else [-1]

print(solution([5,9,7,10],5)) # [5,10]
print(solution([2,36,1,3],1)) # [1,2,3,36]
print(solution([3,2,6],5)) # [-1]
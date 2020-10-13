# 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if answer[-1] != arr[i]: answer.append(arr[i])
    return answer

print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # [4,3]
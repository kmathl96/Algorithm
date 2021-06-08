# 제일 작은 수 제거하기

def solution(arr):
    if len(arr) == 1: return [-1] # arr의 원소가 하나이면 [-1] 반환
    arr.pop(arr.index(min(arr))) # arr의 최솟값의 index 값에 해당하는 요소 제거
    return arr

print(solution([4,3,2,1])) # [4,3,2]
print(solution([10])) # [-1]
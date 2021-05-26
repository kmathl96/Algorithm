# 최솟값 만들기

def solution(A,B):
    answer = 0
    A.sort() # 오름차순으로 정렬
    B.sort(reverse=1) # 내림차순으로 정렬
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer

print(solution([1, 4, 2], [5, 4, 4])) # 29
print(solution([1, 2], [3, 4])) # 10
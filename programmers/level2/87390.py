# n^2 배열 자르기

def solution(n, left, right):
    answer = [] # 1차원 배열
    for i in range(left,right+1):
        # 행 번호와 열 번호 중 더 큰 값을 가짐
        answer.append(max(i//n+1,i%n+1))
    return answer

print(solution(3, 2, 5)) # [3,2,2,3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]
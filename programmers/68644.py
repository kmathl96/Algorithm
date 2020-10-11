# 두 개 뽑아서 더하기
# 월간 코드 챌린지 시즌1
# answer를 (1) list로 선언하고 not in으로 판단해서 append하는 것보다 (2) set로 선언해서 add한 뒤 list로 변환하여 return하는 것이 빠름

def solution(numbers):
    answer = set()
    N = len(numbers)
    for i in range(N-1):
        for j in range(i+1,N):
            tmp = numbers[i]+numbers[j]
            answer.add(tmp)
    return sorted(list(answer))

numbers = [2,1,3,4,1]
print(solution(numbers))
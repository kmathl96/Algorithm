# 구명보트
# 탐욕법(Greedy)

def solution(people, limit):
    answer = 0
    people.sort()
    idx = 0 # 제일 가벼운 사람
    for i in range(len(people)-1,-1,-1): # 제일 무거운 사람부터 태우기
        if people[idx] + people[i] <= limit: # 제일 가벼운 사람이랑 같이 탈 수 있는 경우
            idx += 1 # 그 다음 가벼운 사람의 index 값 저장
        answer += 1 # 구명보트 개수 +1
        if idx >= i: # 모두 다 태운 경우 답 리턴
            return answer

print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3
# 더 맵게
# 힙(Heap)

import heapq

def solution(scoville, K):
    answer = 0 # 섞은 횟수
    heapq.heapify(scoville) # 최소 힙으로 변환
    while len(scoville) > 1: # 음식 개수가 1이 될 때까지 섞기 반복
        # heappop으로 최솟값 2개 가져와서, 섞음 음식의 스코빌 지수 계산
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1 # 섞은 횟수 갱신
        if scoville[0] >= K: return answer # 스코빌 지수의 최솟값이 K 이상 되면 종료
    return -1

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2
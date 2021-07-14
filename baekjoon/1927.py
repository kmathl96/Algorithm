# 최소 힙

import heapq,sys
input = sys.stdin.readline # sys의 input으로 받지 않으면 시간 초과

N = int(input()) # 연산의 개수
nums = [int(input()) for _ in range(N)] # 연산에 대한 정보를 나타내는 정수 리스트
heap = [] # 빈 배열
for x in nums:
    if x: heapq.heappush(heap, x) # x가 자연수라면, 배열에 x 추가
    # x가 0인 경우
    elif heap: print(heapq.heappop(heap)) # 배열에서 가장 작은 값 출력 및 제거
    else: print(0) # 배열이 비어있다면, 0 출력
# 최대 힙
# heapq는 오름차순 정렬하므로,
# 값을 음수로 바꿔서 배열에 저장하면 내림차순 정렬됨 (절대값)
# 꺼낼 때 다시 양수로 바꿈

import heapq,sys
input = sys.stdin.readline

N = int(input()) # 연산의 개수
nums = [int(input()) for _ in range(N)] # 연산할 정수
heap = [] # 빈 배열
for x in nums:
    if x: heapq.heappush(heap, -x) # 자연수인 경우 배열에 x 추가
    elif heap: print(-heapq.heappop(heap)) # 최솟값을 꺼내 다시 양수로 바꿔 출력
    else: print(0) # 배열이 비어있는 경우, 0 출력
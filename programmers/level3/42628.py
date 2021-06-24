# 이중우선순위큐
# 힙(Heap)

import heapq

def solution(operations):
    min_heap,max_heap = [],[] # 최소 힙, 최대 힙
    N = 0 # 큐의 요소 개수
    for operation in operations:
        cmd,num = operation.split() # 명령어, 데이터
        num = int(num)
        if cmd=='I': # 숫자 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num) # 절대값으로 생각하면 내림차순으로 정렬됨
            N += 1 # 큐의 요소 개수 갱신
        elif N:
            # 최댓값 삭제 : 최대 힙에서 pop한 수를 최소 힙에서 삭제
            if num == 1: min_heap.remove(-heapq.heappop(max_heap))
            # 최솟값 삭제 : 최소 힙에서 pop한 수를 최대 힙에서 삭제
            else: max_heap.remove(-heapq.heappop(min_heap))
            N -= 1 # 큐의 요소 개수 갱신
    return [-max_heap[0],min_heap[0]] if N else [0,0] # 큐가 비어있지 않은 경우 [최댓값, 최솟값]을 반환

print(solution(["I 16","D 1"])) # [0,0]
print(solution(["I 7","I 5","I -5","D -1"])) # [7,5]

print(solution(["I 4","I 3","I 2","I 1","D 1","D 1","D -1","D -1","I 5","I 6"])) # [6,5]
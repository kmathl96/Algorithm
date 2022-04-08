# 절댓값 힙
# 자료 구조, 우선순위 큐

import sys,heapq
input = sys.stdin.readline

N = int(input()) # 연산의 개수
heap = [] # 절댓값 힙
ans = [] # 출력할 결과를 담을 리스트

# 연산 수행
for _ in range(N):
    x = int(input()) # 연산에 대한 정보

    # 1. x가 0이 아닌 경우, 배열에 정수 x를 넣음
    if x:
        heapq.heappush(heap,(abs(x),x))

    # 2. 배열에서 절댓값이 가장 작은 값 출력하고, 그 값을 배열에서 제거
    #    절댓값이 가장 작은 값이 여러 개일 때는, 가장 작은 수를 처리
    #    배열이 비어 있는 경우, 0 출력
    else:
        ans.append(str(heapq.heappop(heap)[1]) if heap else '0')

# 한 줄에 하나씩 출력
print('\n'.join(ans))
# 가운데를 말해요
# 자료 구조, 우선순위 큐

import sys,heapq
input = sys.stdin.readline

N = int(input()) # 백준이가 외치는 정수의 개수

# 최대 힙, 최소 힙 사용
# 숫자들을 반씩 번갈아가면서 넣을 것임
# 중간값 이하의 값은 최대 힙에, 이상의 값은 최소 힙에 들어가도록 함
left,right = [],[]

ans = [] # 백준이의 동생이 말해야 하는 수를 넣을 리스트
for i in range(N):
    num = int(input()) # 백준이가 외치는 정수

    # 최대 힙에 넣기
    if i&1:
        heapq.heappush(right, num)
    # 최소 힙에 넣기
    else:
        heapq.heappush(left, -num)
    
    # 최대 힙의 수가 최소 힙의 수보다 큰 경우, 두 수를 바꾸어야 함
    if i and -left[0] > right[0]:
        l,r = heapq.heappop(left),heapq.heappop(right)
        heapq.heappush(left,-r) # 최소 힙의 가장 작은 수를 최대 힙에 넣기
        heapq.heappush(right,-l) # 최대 힙에서 가장 큰 수를 최소 힙에 넣기
    
    # 백준이의 동생이 말해야 할 중간값(최대 힙의 가장 큰 수)을 넣기
    ans.append(str(-left[0]))

# 결과를 순서대로 출력
print('\n'.join(ans))
# 카드 정렬하기
# 자료 구조, 그리디, 우선순위 큐

import sys,heapq
input = sys.stdin.readline

def sol():
    N = int(input()) # 숫자 카드 묶음의 개수
    nums = [int(input()) for _ in range(N)] # 숫자 카드 묶음의 크기
    heapq.heapify(nums) # 힙으로 정렬
    ans = 0 # 최소 비교 횟수

    # 한 묶음이 될 때까지 카드 묶음을 합침
    while len(nums)>1:
        # 가장 작은 카드 수를 가진 두 묶음을 합침
        cnt = heapq.heappop(nums) + heapq.heappop(nums) # 비교 횟수
        ans += cnt # 최소 비교 횟수 증가
        heapq.heappush(nums, cnt) # 힙에 다시 넣기
    
    print(ans)

sol()
# 숫자 카드 2

### 1. 딕셔너리를 활용한 풀이 ###
input() # 가지고 있는 카드의 개수
cards = list(map(int,input().split())) # 카드 리스트
input() # 주어진 정수의 개수
nums = list(map(int,input().split())) # 주어진 정수 리스트

# 숫자 카드의 개수 구하기
cnt = {} # 특정 숫자가 적힌 카드의 개수
for card in cards:
    if card in cnt: cnt[card] += 1 # 1개 추가
    else: cnt[card] = 1 # 아직 개수를 세지 않은 숫자이므로 1개
# 카드에 적힌 숫자인 경우 그 개수를, 아닌 경우 0을 순서대로 반환
print(' '.join([str(cnt[num]) if num in cnt else '0' for num in nums]))

### 2. 이분 탐색을 활용한 풀이 (시간 초과) ###
# import sys
# input = sys.stdin.readline
# 
# N = int(input())
# cards = sorted(list(map(int,input().split()))) # 가지고 있는 카드를 오름차순 정렬
# M = int(input())
# nums = list(map(int,input().split()))
# ans = [] # 각 수가 적힌 숫자 카드를 몇 개 가지고 있는지 담을 리스트
# for num in nums:
#     start,end = 0,N-1 # 양끝의 index 값
#     while start <= end:
#         mid = (start+end)//2 # 중간 index 값
#         card = cards[mid] # 중간에 있는 카드
#         if num == card: break # 카드와 일치하는 경우, 종료
#         elif num < card: end = mid-1 # 카드가 더 큰 경우, 끝 index 값 갱신
#         else: start = mid+1 # 카드가 더 작은 경우, 시작 index 값 갱신

#     if num != card: ans.append('0') # 카드를 가지고 있지 않으므로 0 넣기
#     else: # 카드를 갖고 있는 경우, 몇 개 있는지 확인
#         l,r = mid,mid # 현재 위치에서 양 옆으로 가면서 확인
#         while start <= l and cards[l-1] == num:
#             l -= 1
#         while r < end and cards[r+1] == num:
#             r += 1
#         ans.append(str(r-l+1)) # 개수 넣기
# print(' '.join(ans))
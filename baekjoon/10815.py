# 숫자 카드
# 이분 탐색

import sys
input = sys.stdin.readline

N = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수
nums = sorted(list(map(int,input().split()))) # 상근이가 가지고 있는 숫자 카드에 적혀있는 정수 리스트
input() # 상근이가 가지고 있는지 판단할 정수의 개수 (사용하지 않을 것이므로 따로 저장하지 않음)
test = list(map(int,input().split())) # 상근이가 가지고 있는지 판단할 정수 리스트
ans = [] # 가지고 있는지 여부를 넣을 리스트
for t in test:
    start,end = 0,N-1 # 양 끝 index 값
    while start<=end:
        mid = (start+end)//2 # 중간 index 값
        mid_num = nums[mid] # 중간 값
        if t == mid_num: break # 일치하는 경우, 가지고 있다는 뜻이므로 종료
        elif t < mid_num: end = mid-1 # 중간 값보다 작은 경우, 끝값 갱신
        else: start = mid+1 # 중간 값보다 큰 경우, 시작값 갱신

    # 가지고 있는지 여부(True/False)를 정수형(1/0)으로 바꾼 후
    # 출력할 때 용이하도록 문자형으로 바꿈
    ans.append(str(int(t==mid_num)))
print(' '.join(ans)) # 각 요소들을 공백을 두고 출력
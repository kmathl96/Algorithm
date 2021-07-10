# 수 찾기
# 이분 탐색

### 1. 이분 탐색을 이용한 풀이 ###
N = int(input()) # 리스트 A의 크기
A = sorted(list(map(int,input().split()))) # 정수 리스트 (오름차순 정렬)
input() # 리스트 nums의 크기 (사용하지 않기 때문에 변수에 할당하지 않음)
nums = list(map(int,input().split())) # A에 존재하는지 알아낼 정수 리스트
for num in nums:
    ans,s,e = 0,0,N-1 # 존재하는지 여부, A의 최솟값(s)과 최댓값(e)의 index 값
    while s<=e:
        m = (s+e)//2 # 중간값의 index 값
        if num == A[m]: # 중간값과 일치하는 경우, 존재 여부 변경 후 종료
            ans = 1
            break
        elif num < A[m]: e = m-1 # 중간값보다 작은 경우, 끝 index 값(e) 갱신
        else: s = m+1 # 중간값보다 큰 경우, 시작 index 값(s) 갱신
    print(ans) # 존재 여부 출력

### 2. set를 이용한 풀이 ###
# input()
# A = set(map(int,input().split()))
# input()
# nums = list(map(int,input().split()))
# for num in nums:
#     print(int(num in A)) # 존재하는지 여부를 정수형으로 출력
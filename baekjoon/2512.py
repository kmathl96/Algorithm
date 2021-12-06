# 예산
# 이분 탐색, 매개 변수 탐색

N = int(input()) # 지방의 수
budgets = sorted(list(map(int,input().split()))) # 각 지방이 요청한 예산
M = int(input()) # 국가예산의 총액

if budgets[-1] <= M//N: print(budgets[-1])
else:
    # 이분 탐색 : 상한액 찾기
    left,right = 0,budgets[-1] # 상한액의 최솟값과 최대값
    while left <= right:
        mid = (left+right)//2 # 중간값 (= 상한액)
        
        # 예산 배정하기
        temp = 0 # 배정할 예산
        for i in range(N):
            # 상한액보다 작으면 요청한 만큼 배정
            if budgets[i] < mid:
                temp += budgets[i]
            else: break
        temp += mid*(N-i) # 상한액 이상이면 상한액 만큼 배정

        # 배정한 예산이 총액보다 큰 경우 오른쪽 값을 변경, 작은 경우 왼쪽 값 변경
        if temp > M: right = mid-1
        elif temp <= M: left = mid+1
    print(right)
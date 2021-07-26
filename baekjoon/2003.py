# 수들의 합 2
# 투 포인터

N,M = map(int,input().split()) # 수열의 크기, 만들 부분합
A = list(map(int,input().split())) # 수열
i,j = 0,1 # 부분 수열(A[i]~A[j-1])을 만들 시작/끝 포인터
ans = 0 # 수열의 부분합이 M이 되는 경우의 수
while j<=N: # 끝 포인터가 수열 내에 있는 동안 반복
    sum_ = sum(A[i:j]) # A[i]~A[j-1]의 합
    if sum_ >= M and i < j: # 합이 M 이상이고 i가 j보다 작은 경우
        i += 1 # 시작 포인터를 오른쪽으로 이동
        if sum_ == M: ans += 1 # 합이 M이면 경우의 수 증가
    else: j += 1 # 합이 M 미만인 경우, 끝 포인터를 오른쪽으로 이동
print(ans)
# 부분합
# 투 포인터

N,S = map(int,input().split()) # 수열의 길이, 만족해야 하는 수
nums = list(map(int,input().split())) # 수열
i,j = 0,1 # 부분합 구간([i,j))의 양 끝을 가리키는 포인터
sub = nums[0] # 부분합 : [0,1)의 합으로 초기화

# 부분합이 S 이상인 구간의 길이 중 최솟값
# 수열의 길이의 최댓값이 100000이므로 그보다 큰 값으로 초기화 
answer = 100001

while True:
    # 부분합이 S 이상인 경우
    if sub >= S:
        answer = min(answer, j-i) # answer 갱신

        # 왼쪽 포인터를 이동해도 유효한 부분 구간인 경우
        if i+1 < j:
            sub -= nums[i] # i번째 수만큼 부분합 감소
            i += 1 # 왼쪽 포인터 이동
            continue
    
    # 부분합이 S 미만이거나 왼쪽 포인터를 움직이지 못한 경우
    if j == N: break # 오른쪽 포인터가 끝에 있다면 종료
    sub += nums[j] # j번째 수만큼 부분합 증가
    j += 1 # 오른쪽 포인터 이동
print(0 if answer==100001 else answer) # 초기값과 같다면 0

# ex1)
# 1 1
# 1
# => 1

# ex2)
# 10 10
# 1 1 1 1 1 1 1 1 1 1
# => 10
# 극장 좌석
# 다이나믹 프로그래밍

N = int(input()) # 좌석의 개수
M = int(input()) # 고정석의 개수

# 고정석 번호 저장
fixed = [0]*(N+1) # 각 좌석의 고정 여부
fixed[0] = 1
for _ in range(M):
    fixed[int(input())] = 1

# 1번 좌석부터 각각의 좌석까지, 좌석에 앉을 수 있는 방법의 가짓수
dp = [0]*(N+1)
dp[0] = 1

for i in range(1,N+1):
    # 앞 좌석(i-1)이 고정석이거나 해당 좌석(i)이 고정석인 경우
    # => 해당 좌석에는 i번 입장권을 가진 사람만 앉을 수 있음
    # => 앞 좌석의 경우의 수와 같음
    if fixed[i-1] or fixed[i]:
        dp[i] = dp[i-1]
    # 앞 좌석과 바꿔앉을 수 있는 경우
    # 1. 그대로 앉음 => 앞 좌석의 경우의 수와 같음
    # 2. i-1와 i가 바꿔앉음 => 앞앞 좌석의 경우의 수와 같음
    else:
        dp[i] = dp[i-2]+dp[i-1]

# N번 좌석까지 계산했을 때의 결과 출력
print(dp[N])
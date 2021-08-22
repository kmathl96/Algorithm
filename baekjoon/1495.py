# 기타리스트
# 다이나믹 프로그래밍

N,S,M = map(int,input().split()) # 곡의 개수, 시작 볼륨, 볼륨의 최댓값
V = list(map(int,input().split())) # V[i] = i번째 곡 시작 전에 바꿀 수 있는 볼륨
dp = [[0]*(M+1) for _ in range(N+1)] # dp[r][c] = r번째 곡을 c 볼륨으로 연주할 수 있는지 여부
dp[0][S] = 1 # S 크기의 볼륨으로 시작
for i in range(N):
    for vol in range(M+1):
        if dp[i][vol]:
            # 그 다음 곡을 연주할 수 있는 볼륨 체크
            if vol+V[i] < M+1: dp[i+1][vol+V[i]] = 1
            if vol-V[i] >= 0: dp[i+1][vol-V[i]] = 1

# 가능한 마지막 곡의 볼륨 중 최댓값 출력
answer = -1 # 마지막 곡을 연주할 수 없다면 -1을 출력해야 하므로 -1로 초기화
for i in range(M,-1,-1): # 끝 열부터 확인
    # 마지막 곡을 연주할 수 있는 볼륨인 경우, answer 변경 후 종료
    if dp[N][i]:
        answer = i
        break
print(answer)
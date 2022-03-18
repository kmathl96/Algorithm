# 상자넣기
# 다이나믹 프로그래밍

n = int(input()) # 상자의 개수
box = list(map(int,input().split())) # 각 상자의 크기

# 최대로 넣을 수 있는 상자 개수 : 자기 자신을 포함해서 세므로 1로 초기화
dp = [1]*n

for i in range(1,n):
    # 앞의 상자들 확인
    for j in range(i):
        # 현재 상자보다 작은 경우
        if box[i] > box[j]:
            # 해당 상자를 넣는 것이 현재 저장된 개수와 비교하여 더 큰 값 저장
            dp[i] = max(dp[i],dp[j]+1)

# 한 번에 넣을 수 있는 최대의 상자 개수 출력
print(max(dp))
# 가장 긴 감소하는 부분 수열
# 다이나믹 프로그래밍

N = int(input())
A = list(map(int,input().split()))
ans = [1]*N # 자기 혼자만 부분 수열을 구성할 경우 1이므로 1로 초기화
for i in range(1,N):
    for j in range(i):
        # 자기보다 클 경우
        # 그 부분 수열의 길이 + 1와, 현재 자기의 부분 수열의 길이와 비교하여 더 큰 값 저장
        if A[j] > A[i]: ans[i] = max(ans[i],ans[j]+1)
print(max(ans))
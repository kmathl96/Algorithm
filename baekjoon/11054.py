# 가장 긴 바이토닉 부분 수열
# 다이나믹 프로그래밍

N = int(input())
A = list(map(int,input().split()))

# 가장 긴 증가/감소 부분 수열 길이
# 증가 부분 수열은 자신을 포함시켜서 계산하므로 1로 초기화
# 중복 계산되지 않도록 감소 부분 수열은 자신을 포함시키지 않으므로 0으로 초기화
inc,dec = [1]*N,[0]*N

for i in range(N):
    for j in range(i):
        # 가장 긴 증가 부분 수열 (앞에서부터 저장)
        if A[j] < A[i] and inc[j]+1 > inc[i]:
            inc[i] = inc[j]+1
        # 가장 긴 감소 부분 수열 (뒤에서부터 저장)
        if A[N-j-1] < A[N-i-1] and dec[N-j-1]+1 > dec[N-i-1]:
            dec[N-i-1] = dec[N-j-1]+1

# 각 수열의 길이를 더한 값 중 최댓값 출력
print(max([inc[k]+dec[k] for k in range(N)]))
# 보물
# 수학, 그리디, 정렬

N = int(input()) # 정수 배열 A, B의 길이
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))

# S = A[0]*B[0] + ... + A[N-1]*B[N-1] 의 최솟값 구하기
# => 가장 큰 값과 가장 작은 값을 순서대로 곱해서 더하기
print(sum(A[i]*B[N-1-i] for i in range(N)))
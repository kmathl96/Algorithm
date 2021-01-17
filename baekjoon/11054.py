N = int(input())
A = list(map(int,input().split()))
inc,dec = [1]*N,[0]*N
for i in range(N):
    for j in range(i):
        if A[j] < A[i] and inc[j]+1 > inc[i]:
            inc[i] = inc[j]+1
        if A[N-j-1] < A[N-i-1] and dec[N-j-1]+1 > dec[N-i-1]:
            dec[N-i-1] = dec[N-j-1]+1
print(max([inc[k]+dec[k] for k in range(N)]))
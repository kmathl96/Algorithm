# 이차원 배열과 연산
# 구현, 시뮬레이션

# R 연산
def r_op():
    mx_len = 0 # 열 개수가 가장 큰 행을 기준으로 0을 채우기 위한 변수
    for i in range(len(A)):
        cnt = set() # 각 수의 개수를 담을 set
        for n in A[i]:
            # 0보다 큰 경우 set에 해당 수와 그 수의 개수를 넣음
            if n: cnt.add((n,A[i].count(n)))
        A[i] = [] # 원래 행 초기화
        # 각 수의 개수와 크기 기준으로 cnt를 정렬한후 순서대로 원래 행에 넣음
        for n,c in sorted(list(cnt), key=lambda x: (x[1],x[0])):
            A[i].append(n) # 해당 수
            A[i].append(c) # 해당 수의 개수
            if len(A[i])==100: break # 100을 넘길 경우 버림
        mx_len = max(mx_len, len(A[i]))
    for row in A:
        row += [0]*(mx_len-len(row)) # 최대 열 개수 만큼 0 채움

# 행렬 반전
def rotate(A):
    return [[A[r][c] for r in range(len(A))] for c in range(len(A[0]))]

r,c,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(3)]
time = 0
while time<101:
    if r-1<len(A) and c-1<len(A[0]) and A[r-1][c-1]==k: break
    # 열 개수가 행 개수보다 큰 경우 C 연산
    # 행렬을 반전시키고 R 연산을 한 뒤 다시 반전시킨 것과 같음
    if len(A[0])>len(A):
        A = rotate(A)
        r_op()
        A = rotate(A)
    # 행 개수가 열 개수보다 많거나 같은 경우 R 연산
    else: r_op()
    time += 1
print(time if time<101 else -1)
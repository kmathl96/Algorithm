# 배열 돌리기 3
# 구현

# 연산 번호에 따라 배열을 돌리는 함수
def rot(num,N,M):
    global A

    # 1번 연산 : 배열을 상하 반전시키는 연산
    if num == 1:
        A = A[::-1]
    
    # 2번 연산 : 배열을 좌우 반전시키는 연산
    if num == 2:
        A = [row[::-1] for row in A]
    
    # 3번 연산 : 오른쪽으로 90도 회전시키는 연산
    if num == 3:
        A = [[A[N-1-r][c] for r in range(N)] for c in range(M)]
    
    # 4번 연산 : 왼쪽으로 90도 회전시키는 연산
    if num == 4:
        A = [[A[r][M-1-c] for r in range(N)] for c in range(M)]
    
    # 5, 6번 연산은 배열을 N/2*M/2인 4개의 부분 배열로 나눠서 수행
    # 5번 연산 : 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산
    if num == 5:
        for r in range(N//2):
            for c in range(M//2):
                A[r][c],A[r][c+M//2],A[r+N//2][c+M//2],A[r+N//2][c] = A[r+N//2][c],A[r][c],A[r][c+M//2],A[r+N//2][c+M//2]
    
    # 6번 연산 : 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산
    if num == 6:
        for r in range(N//2):
            for c in range(M//2):
                A[r][c],A[r][c+M//2],A[r+N//2][c+M//2],A[r+N//2][c] = A[r][c+M//2],A[r+N//2][c+M//2],A[r+N//2][c],A[r][c]

N,M,R = map(int,input().split()) # 배열의 크기와 수행해야 하는 연산의 수
A = [list(map(int,input().split())) for _ in range(N)] # 배열
cmds = list(map(int,input().split())) # 수행해야 하는 연산

# 연산을 순서대로 수행
for cmd in cmds:
    rot(cmd,len(A),len(A[0]))

# 결과를 출력
for row in A:
    print(*row)
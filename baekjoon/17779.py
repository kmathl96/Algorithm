# 게리맨더링 2
# 구현, 브루트 포스, 시뮬레이션

def f(x,y,d1,d2):
    global ans
    p = [0]*5 # 각 선거구의 인구 수
    last = [[0]*N for _ in range(N)] # 마지막 구의 경계이면 1, 아니면 0
    # 마지막 구 경계 표시
    for i in range(d1+1):
        last[x+i][y-i] = 1
        last[x+d2+i][y+d2-i] = 1
    for i in range(d2+1):
        last[x+i][y+i] = 1
        last[x+d1+i][y-d1+i] = 1
    # 각 선거구의 인구 수 계산 : 경계를 만나면 다음 행 탐색
    # 1번 선거구 : 왼쪽 위부터 탐색
    for r in range(x+d1):
        for c in range(y+1):
            if last[r][c]: break
            p[0] += A[r][c]
    # 2번 선거구 : 오른쪽 위부터 탐색
    for r in range(x+d2+1):
        for c in range(N-1,y,-1): # 맨오른쪽 열부터 왼쪽 방향으로 탐색
            if last[r][c]: break
            p[1] += A[r][c]
    # 3번 선거구 : 왼쪽 경계선이 꺾이는 부분부터 탐색
    for r in range(x+d1,N):
        for c in range(y-d1+d2):
            if last[r][c]: break
            p[2] += A[r][c]
    # 4번 선거구 : 오른쪽 경계선이 꺾이는 부분부터 탐색
    for r in range(x+d2+1,N):
        for c in range(N-1,y-d1+d2-1,-1):
            if last[r][c]: break
            p[3] += A[r][c]
    # 5번 선거구 : 총 인구 수에서 1~4번 선거구 인구 수 뺀 값
    p[4] = all_sum - sum(p)
    ans = min(ans,max(p)-min(p)) # 최솟값 갱신

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
ans = 40000 # 인구 수 차이의 최솟값 초기화
all_sum = sum([sum(A[r]) for r in range(N)]) # 총 인구 수
# 1. 기준점 x, y
for x in range(N-2): # x은 d1,d2가 최솟값(1)일 때 N-3행에 위치할 수 있음
    for y in range(1,N-1): # y는 d1이 최솟값일 때 1열, d2이 최솟값일 때 N-2열에 위치할 수 있음
        # 경계의 길이 d1, d2
        for d1 in range(1,y+1):
            # d2의 최댓값은, y 기준 오른쪽에 남은 만큼과 x+d1 기준 아래쪽에 남은 만큼 중 작은 값
            for d2 in range(1,min(N-d1-x,N-y)):
                f(x,y,d1,d2)
print(ans)
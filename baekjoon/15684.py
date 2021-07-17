# 사다리 조작
# 구현, 브루트포스, 백트래킹

# i번 세로선의 결과가 i번이 나오는지 확인
def isCorrect(conn):
    # 모든 세로선에 대해 확인
    for col in range(1,N+1):
        cur_line = col # 현재 위치
        for r in range(1,H+1):
            # 이전 세로선과 연결되어 있다면 현재 위치를 이전 세로선으로 이동
            if conn[r][cur_line-1]: cur_line -= 1
            # 다음 세로선과 연결되어 있다면 현재 위치를 다음 세로선으로 이동
            elif conn[r][cur_line]: cur_line += 1
            
            # 현재 위치와 원래 위치와의 간격이 남은 행보다 큰 경우, 원래 위치로 갈 수 없으므로 False 반환
            if abs(cur_line-col) > H-r: return False
        if cur_line != col: return False # 도착지가 원래 위치가 아닌 경우 False 반환
    return True

# 가로선 추가하며 모든 경우 탐색
def f(row,cnt,conn):
    global ans
    if isCorrect(conn): # 문제의 조건을 만족하는 경우 종료
        if ans > cnt: ans = cnt # 추가한 가로선 개수가 더 적으면 갱신
        return
    if cnt > 2 or ans <= cnt: return
    for r in range(row,H+1): # 현재 행부터 끝까지 탐색하며 가로선 추가
        for c in range(1,N):
            # 현재 세로선과 다음 세로선과 연결이 되어있거나
            # 다음 세로선이 그다음 세로선과 연결이 되어있거나
            # 현재 세로선과 이전 세로선이 연결되어 있는 경우,
            # 가로선을 추가할 수 없으므로 넘어감
            if conn[r][c] or conn[r][c+1] or (c > 1 and conn[r][c-1]): continue
            conn[r][c] = 1 # 가로선 추가
            f(r,cnt+1,conn) # 탐색 반복
            conn[r][c] = 0 # 가로선 다시 원상태로

N,M,H = map(int,input().split()) # 세로선의 개수, 가로선의 개수, 세로선마다 가로선을 놓을 수 있는 위치의 개수
conn = [[0]*(N+1) for _ in range(H+1)] # 다음 세로선과의 연결 여부
for i in range(M):
    a,b = map(int,input().split()) # 가로선의 정보
    conn[a][b] = 1 # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결
ans = 4 # 추가해야 하는 가로선 개수의 최솟값 (3보다 큰 값이면 -1을 출력하는 것이므로 4로 초기화)
f(1,0,conn) # 현재 행, 추가한 가로선 개수, 연결 리스트
print(ans if ans!=4 else -1) # ans가 4(초기화했었던 값)이면 -1 출력, 아니면 ans 출력
# N-Queen
# 브루트포스, 백트래킹

# r행에 퀸 놓기
def put(r):
    global ans

    # 체스판의 모든 행에 퀸을 놓은 경우, 경우의 수를 증가시킨 후 종료
    if r==N:
        ans += 1
        return
    
    # 모든 열 탐색
    for c in range(N):
        # 다른 행에서 이미 해당 열에 퀸을 놓은 경우 넘어감
        if visited[c]: continue

        # 해당 칸의 대각선에 다른 퀸이 있는지 탐색
        flag = 0 # 존재 여부
        for i in range(1,r+1):
            # 왼쪽 대각선이나 오른쪽 대각선에 존재하는 경우
            if (0<=c-i and chess[r-i][c-i]) or (c+i<N and chess[r-i][c+i]):
                # 존재 여부 변경 후 종료
                flag = 1
                break
        if flag: continue # 다른 퀸이 있다면 해당 칸은 퀸을 놓지 않고 넘어감
        
        # 해당 좌표에 퀸 놓기
        chess[r][c],visited[c] = 1,1 # 체스판과 열 방문 리스트 체크
        put(r+1) # 다음 행에 퀸 놓기
        chess[r][c],visited[c] = 0,0 # 다시 0으로 변경

N = int(input()) # 체스판의 크기
visited = [0]*N # 각 열의 퀸의 존재 여부
chess = [[0]*N for _ in range(N)] # 체스판 각 칸의 퀸의 존재 여부
ans = 0 # 퀸을 서로 공격할 수 없게 놓는 경우의 수
put(0) # 0행부터 퀸 놓으면서 ans 갱신하기
print(ans)
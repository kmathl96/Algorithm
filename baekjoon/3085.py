# 사탕 게임
# 구현, 브루트포스

# 가장 긴 연속 부분의 길이 찾기
def find(board):
    max_cnt = 0 # 같은 색인 연속된 사탕 개수
    for r in range(N):
        for c in range(N):
            # 남은 행/열 길이가 더 작으면 탐색할 필요가 없으므로 종료
            if max_cnt >= N-r and max_cnt >= N-c: break
            row_cnt,col_cnt = 1,1 # 행/열 개수
            
            # 밑으로 탐색
            for row in range(r+1,N):
                if board[r][c] != board[row][c]: break
                row_cnt += 1
            
            # 오른쪽으로 탐색
            for col in range(c+1,N):
                if board[r][c] != board[r][col]: break
                col_cnt += 1
            
            max_cnt = max(max_cnt,row_cnt,col_cnt) # 제일 큰 값 저장
    return max_cnt

N = int(input()) # 보드의 크기
board = [list(input()) for _ in range(N)] # 보드에 채워져 있는 사탕의 색상
answer = 0 # 상근이가 먹을 수 있는 사탕의 최대 개수
d = [(0,1),(1,0)] # 방향
for r in range(N):
    for c in range(N):
        # 해당 위치에서 인접한 칸(오른쪽/밑)과 교환
        for i in range(2):
            nr,nc = r+d[i][0],c+d[i][1] # 인접 칸의 위치
            # 다른 색상인 경우
            # 교환한 후 answer를 갱신하고 다시 원위치로 변경
            if nr<N and nc<N and board[r][c] != board[nr][nc]:
                board[r][c],board[nr][nc] = board[nr][nc],board[r][c]
                answer = max(answer,find(board))
                board[r][c],board[nr][nc] = board[nr][nc],board[r][c]
print(answer)
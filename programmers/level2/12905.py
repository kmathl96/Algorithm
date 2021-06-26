# 가장 큰 정사각형 찾기

def solution(board):
    answer = 0 # 1로 이루어진 가장 큰 정사각형의 길이 : 0으로 초기화

    # board의 각 위치에서 가능한 정사각형의 최대 길이 갱신
    for r in range(len(board)):
        for c in range(len(board[0])):
            if r and c and board[r][c]:
                # (r,c)에서의 최대 길이 = 직전 위치((r-1,c-1),(r-1,c),(r,c-1)) 중 최솟값 + 1
                board[r][c] = min(board[r-1][c-1],board[r-1][c],board[r][c-1])+1
            # 해당 값이 answer보다 크면 answer 갱신
            if board[r][c] > answer: answer = board[r][c]
    return answer**2 # 길이를 제곱하여 정사각형의 넓이 반환

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])) # 9
print(solution([[0,0,1,1],[1,1,1,1]])) # 4

print(solution([[1,0],[0,0]])) # 1
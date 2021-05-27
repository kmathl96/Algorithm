# [1차] 프렌즈4블록
# 2018 KAKAO BLIND RECRUITMENT

# 4블록을 찾아 지우고 블록을 옮김
def game(m, n, board):
    remove = [[0]*m for _ in range(n)] # 어떤 블록이 지워지는지 저장
    cnt = 0 # 지워진 블록 개수
    for r in range(1,n):
        for c in range(1,m):
            if not board[r][c]: continue # 빈 자리(0)는 넘어감
            if board[r-1][c-1] == board[r-1][c] == board[r][c-1] == board[r][c]:
                remove[r-1][c-1],remove[r-1][c],remove[r][c-1],remove[r][c] = 1,1,1,1
    for r in range(n):
        # 앞 열부터 처리하면 index 값 때문에 뒷 열 처리가 복잡해지므로 뒷 열부터 처리
        for c in range(m-1,-1,-1):
            if remove[r][c]:
                board[r].pop(c) # 해당 블록 삭제
                board[r].append(0) # 빈 공간을 0으로 채움
                cnt += 1
    return cnt # 지워진 블록 개수 반환

def solution(m, n, board):
    # 처리를 쉽게 하기 위해 board를 변경
    # 지워진 후 블록들이 아래 방향으로 떨어지는 게 아니라 왼쪽으로 옮겨지도록
    board = [[board[m-j-1][i] for j in range(m)] for i in range(n)]

    answer = 0 # 지워진 블록 개수
    while True:
        cnt = game(m, n, board)
        if not cnt: break # 지워진 블록이 없으면 종료
        answer += cnt # 총 지워진 블록 개수 갱신
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15
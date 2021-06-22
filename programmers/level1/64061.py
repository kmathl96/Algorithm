# 크레인 인형뽑기 게임
# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    answer = 0 # 사라진 인형의 개수
    st = [] # 뽑은 인형을 넣을 바구니
    N = len(board) # 인형뽑기 크기

    # 처리하기 쉽도록 board 바꾸기
    # 인형 뽑는 것을 pop으로 처리하기 위해, 왼쪽이 인형뽑기의 바닥이 되게 함
    new_board = [[] for _ in range(N)]
    for c in range(N):
        for r in range(N):
            cur = board[N-1-r][c]
            if not cur: break # 0이면 인형을 더 넣지 않고 다음 위치로 이동
            new_board[c].append(cur)
    
    for move in moves:
        if not new_board[move-1]: continue # 해당 위치에 인형이 없으면 넘어감
        pick = new_board[move-1].pop() # 인형을 꺼냄
        if st and st[-1]==pick: # 바구니의 맨 윗 인형과 같은 경우
            st.pop() # 바구니에서 해당 인형을 없앰
            answer += 2 # 사라진 인형 개수 갱신 (2개)
        else: st.append(pick) # 바구니의 맨 윗 인형과 다른 경우 바구니에 인형을 넣음
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # 4
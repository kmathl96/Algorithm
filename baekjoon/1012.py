# 유기농 배추
# DFS

import sys
input = sys.stdin.readline

ans = [] # 각 테스트 케이스의 결과를 넣을 리스트
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열

# 입력된 테스트 케이스의 개수 만큼 반복
for _ in range(int(input())):
    M,N,K = map(int,input().split()) # 배추밭의 가로길이와 세로길이, 배추가 심어져 있는 위치의 개수
    board = [[0]*M for _ in range(N)] # 배추밭 : 각 칸에 배추가 심어져있는지 여부를 저장
    for _ in range(K):
        X,Y = map(int,input().split()) # 배추의 위치
        board[Y][X] = 1

    # 배추를 해충으로부터 보호하기 위해 필요한 최소의 배추흰지렁이 마리 수 구하기
    cnt = 0 # 지렁이 마리 수
    st = [] # 스택
    
    # 각 칸을 탐색
    for row in range(N):
        for col in range(M):
            # 배추가 없으면 탐색하지 않음
            if not board[row][col]: continue

            # DFS로 인접한 배추들 탐색하기
            st.append((row,col))
            cnt += 1 # 지렁이 수 증가
            board[row][col] = 0 # 다음에 또 탐색하지 않도록 0으로 변경
            while st:
                r,c = st.pop() # 현재 칸의 좌표
                
                # 인접한 칸 탐색
                for i in range(4):
                    nr,nc = r+dr[i],c+dc[i] # 탐색할 칸의 좌표
                    # 유효한 위치이며 배추가 있는 경우
                    if 0<=nr<N and 0<=nc<M and board[nr][nc]:
                        board[nr][nc] = 0 # 중복 방문 방지
                        st.append((nr,nc)) # 인접한 칸 탐색을 위해 스택에 넣기
    ans.append(cnt) # 지렁이의 마리 수 넣기

# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력
for cnt in ans: print(cnt)
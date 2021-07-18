# 나무 재테크
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split()) # 땅의 크기, 나무의 개수, 시간
A = [list(map(int,input().split())) for _ in range(N)] # 매 겨울 S2D2가 땅에 추가할 양분의 양
board = [[[] for i in range(N+1)] for _ in range(N+1)] # 땅
trees = [list(map(int,input().split())) for _ in range(M)] # 심을 나무의 정보
food = [[5]*(N+1) for _ in range(N+1)] # 양분 : 가장 처음은 모든 칸에 5만큼 들어있음
dr,dc = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1] # 방향

for _ in range(K): # K년 동안 반복
    ans = 0 # 땅에 심어져있는 나무의 개수

    # 나무 심기
    while trees:
        x,y,z = trees.pop() # 좌표와 나이
        board[x][y].append(z)

    # 사계절
    for r in range(1,N+1):
        for c in range(1,N+1):
            # 봄 : 어린 나무부터 양분 먹고 나이 증가
            board[r][c].sort() # 오름차순 정렬
            live,die = [],0 # 양분을 먹은 나무의 나이 리스트, 양분을 먹지 못해 죽은 나무의 나이의 합
            for age in board[r][c]:
                # 땅에 양분이 충분한 경우
                if food[r][c] >= age:
                    food[r][c] -= age # 나이 만큼 양분을 먹음
                    live.append(age+1) # 나이 1 증가
                    # 가을 : 나무 번식
                    if (age+1)%5: continue # 나이가 5의 배수가 아니라면 넘어감
                    for i in range(8):
                        nr,nc = r+dr[i],c+dc[i] # 인접한 칸의 좌표
                        # 좌표가 유효한(= 땅을 벗어나지 않는) 경우, trees에 번식하는 나무(나이=1) 추가
                        if 0<nr<=N and 0<nc<=N: trees.append((nr,nc,1))
                # 땅에 양분이 부족해 양분을 먹을 수 없는 나무는 죽음
                else: die += age//2 # 죽은 나무의 나이를 2로 나눈 값 (양분으로 추가됨)
            board[r][c] = live # 양분을 먹은 나무만 삶
            # 여름 : 죽은 나무는 양분으로 변함 => die
            # 겨울 : S2D2가 각 칸에 양분을 추가함 => A[r-1][c-1]
            food[r][c] += die+A[r-1][c-1]
            ans += len(board[r][c]) # 나무 개수 추가
    if not ans: break # 땅에 나무가 없으면 종료
print(ans+len(trees)) # 살아있는 나무(땅에 있는 나무와 번식하는 나무)의 개수 출력
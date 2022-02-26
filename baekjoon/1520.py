# 내리막 길
# DP, DFS

import sys
sys.setrecursionlimit(10**6) # RecursionError 방지
input = sys.stdin.readline

# (r,c)에서 제일 오른쪽 아래 칸까지의 내리막길로 이동하는 경로 개수 구하기
def dfs(r,c):
    # 아직 방문하지 않은 경우, 탐색하여 경로의 개수 구해서 저장
    if H[r][c]==-1:
        H[r][c] = 0 # 우선 0으로 변경
        
        # 사방 탐색
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치
            
            # 유효한 위치이며 내리막길인 경우
            if 0<=nr<M and 0<=nc<N and board[r][c]>board[nr][nc]:
                H[r][c] += dfs(nr,nc) # 해당 위치의 경로 개수만큼 더하기
    
    return H[r][c] # 경로의 개수 반환

M,N = map(int,input().split()) # 지도의 크기
board = [list(map(int,input().split())) for _ in range(M)] # 각 지점의 높이
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열

# 각 지점에서 제일 오른쪽 아래 지점까지의 경로의 개수
# 경로의 개수가 0인 경우와 헷갈리지 않도록
# 아직 방문하지 않은 지점은 -1로 저장
H = [[-1]*N for _ in range(M)]
H[-1][-1] = 1 # 제일 오른쪽 아래 칸은 1로 저장

# 제일 왼쪽 위 지점에서 제일 오른쪽 아래 지점까지 이동하는 경로의 개수 출력
print(dfs(0,0))
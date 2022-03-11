# 빛의 경로 사이클

# 빛의 경로 사이클 구하기
def find(r,c,i,grid,visited):
    dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 리스트
    N,M = len(grid),len(grid[0]) # 격자의 크기
    leng = 0 # 사이클의 길이

    # 방문했던 경로를 다시 방문할 때까지 반복
    while not visited[r][c][i]:
        visited[r][c][i] = 1 # 방문 체크
        r,c = (r+dr[i])%N,(c+dc[i])%M # 이동할 위치

        # 각 칸에 써진 글자대로 방향을 바꿈 (S인 경우 직진이므로 바꾸지 않음)
        if grid[r][c]=='L': i = (i-1)%4 # 좌회전
        elif grid[r][c]=='R': i = (i+1)%4 # 우회전
        
        leng += 1 # 사이클의 길이 증가
    
    # 빛의 경로 사이클 길이 반환
    return leng

def solution(grid):
    answer = [] # 빛의 경로 사이클의 길이를 담을 리스트
    N,M = len(grid),len(grid[0]) # 격자의 크기

    # 각 칸의 상-우-하-좌 경로의 방문 여부를 체크할 방문 배열
    visited = [[[0]*4 for _ in range(M)] for _ in range(N)]

    # 각 칸에서 출발하는 경로 탐색
    for r in range(N):
        for c in range(M):
            # 네 가지 방향으로 탐색
            for i in range(4):
                # 방문하지 않은 경로인 경우 탐색
                if not visited[r][c][i]:
                    # 빛의 경로 사이클의 길이를 구해서 리스트에 담기
                    answer.append(find(r,c,i,grid,visited))
    
    # 빛의 경로 사이클의 모든 길이들을 오름차순으로 정렬하여 반환
    return sorted(answer)

print(solution(["SL","LR"])) # [16]
print(solution(["S"])) # [1,1,1,1]
print(solution(["R","R"])) # [4,4]
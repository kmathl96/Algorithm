# 달이 차오른다, 가자.
# BFS, 비트마스킹

from collections import deque

N,M = map(int,input().split()) # 미로의 크기
maze = [list(input()) for _ in range(N)] # 미로의 모양
for r in range(N):
    for c in range(M):
        # 민식이의 위치인 경우
        if maze[r][c] == '0':
            sr,sc = r,c # 민식이의 위치 좌표 저장
            maze[sr][sc] = '.' # 빈 칸으로 변경
            break

# BFS로 탐색
q = deque([(sr,sc,0,0)]) # 큐

# 방문 배열
# visited[r][c][key] : (r,c)의 위치에 key와 같은 열쇠를 가지고 방문한 적 있는지 체크
visited = [[[0]*(1<<6) for _ in range(M)] for _ in range(N)]
visited[sr][sc][0] = 1 # 출발 위치(민식이의 위치) 방문 체크

dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
ans = -1 # 미로를 탈출하는 데 걸리는 이동 횟수 : 탈출할 수 없을 경우, -1을 출력해야 하므로 -1로 초기화
while q:
    r,c,d,key = q.popleft() # 현재 위치의 좌표, 이동 횟수, 가지고 있는 열쇠
    
    # 출구인 경우, 탈출(탐색 종료)
    if maze[r][c] == '1':
        ans = d # 답 변경
        break
    
    # 인접한 칸 탐색
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i] # 이동할 위치
        # 유효한 위치이며, 벽(#)이 아니고, 방문한 적 없는 경우
        if 0<=nr<N and 0<=nc<M and maze[nr][nc]!='#' and not visited[nr][nc][key]:
            val,new_key = ord(maze[nr][nc]),key
            
            # 열쇠(a~f)인 경우
            if 97<=val<=102:
                new_key = key|(1<<(val-97)) # 열쇠 획득
            # 문(A~F)이면서 해당 문에 대응하는 열쇠가 없는 경우, 넘어감
            elif 65<=val<=70 and not (1<<(val-65))&key: continue
            
            q.append((nr,nc,d+1,new_key)) # 더 탐색하기 위해 큐에 넣기
            visited[nr][nc][new_key] = 1 # 방문 체크
print(ans)
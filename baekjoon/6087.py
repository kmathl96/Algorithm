# 레이저 통신
# 다익스트라, BFS

import heapq

def dijstra():
    # dist[r][c] : (r,c) 위치로 이동할 수 있는 최소 거울 개수
    dist = [[10000]*W for _ in range(H)]
    dist[sr][sc] = 0 # 시작점은 거울 개수 0

    # 힙에 초기 값 넣기
    heap = []
    for i in range(4):
        heap.append((0,sr,sc,i)) # 거울 개수, 위치, 방향

    dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
    while heap:
        cnt,r,c,d = heapq.heappop(heap)

        # 도착점에 도달한 경우, 거울 개수 반환
        if r==er and c==ec:
            return cnt

        # 이전에 더 적은 거울 개수로 방문한 경우, 더 탐색할 필요가 없으므로 넘어감
        if dist[r][c] < cnt: continue

        # 인접한 칸 탐색
        for i in range(4):
            # 현재 방향과 반대 방향인 경우, 이동할 수 없으므로 넘어감
            if abs(d-i)==2: continue

            new_cnt = cnt # 설치해야 하는 거울 개수
            # 현재 방향과 같지 않은 경우(= 90도 회전), 거울을 설치해야 함
            if i!=d:
                new_cnt += 1 # 거울 개수 증가
            
            nr,nc = r+dr[i],c+dc[i] # 이동할 위치
            # 유효한 위치이며, 빈 칸이고, 거울 개수가 이전보다 적으면, 이동 반복
            while 0<=nr<H and 0<=nc<W and board[nr][nc]=='.' and dist[nr][nc] > cnt:
                dist[nr][nc] = new_cnt # 거울 개수 저장
                heapq.heappush(heap, (new_cnt,nr,nc,i)) # 힙에 넣기
                nr,nc = nr+dr[i],nc+dc[i] # 같은 방향으로 한 칸 더 이동

W,H = map(int,input().split()) # 지도의 크기
board = [list(input()) for _ in range(H)] # 지도

# C의 위치 찾기
pos = [] # C로 표시되어 있는 칸의 위치를 담을 리스트
for r in range(H):
    for c in range(W):
        if board[r][c] == 'C':
            board[r][c] = '.' # 빈 칸으로 표시
            pos.append((r,c)) # 좌표 넣기
(sr,sc),(er,ec) = pos # 시작점과 끝점으로 저장

# 다익스트라로 탐색한 결과 값 출력
print(dijstra())
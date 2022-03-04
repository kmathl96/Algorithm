# 녹색 옷 입은 애가 젤다지?
# 다익스트라

import sys,heapq
input = sys.stdin.readline

def dijkstra():
    # 동굴의 각 칸에 가는 동안 잃는 소지금의 최솟값
    dist = [[1000000]*N for _ in range(N)]

    # 최소 힙 : (해당 칸을 가는 동안 잃는 소지금의 최솟값, 해당 칸의 행과 열의 인덱스 값)
    q = [(cave[0][0],0,0)]
    while q:
        d,r,c = heapq.heappop(q) # 잃는 소지금과 칸의 위치

        # 저장된 값보다 잃는 소지금의 값이 크면 넘어감
        if dist[r][c] < d: continue

        # 인접한 칸을 탐색하여 dist 갱신
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i] # 탐색할 칸
            # 유효한 위치이며, (r,c)를 거쳐서 갈 때 잃는 소지금이 저장된 dist값보다 작은 경우
            if 0<=nr<N and 0<=nc<N and dist[nr][nc] > d+cave[nr][nc]:
                nd = d+cave[nr][nc] # (r,c)를 거쳐서 갈 때 잃는 소지금
                dist[nr][nc] = nd # dist값 갱신
                heapq.heappush(q,(nd,nr,nc)) # 힙에 넣기
    
    # 제일 오른쪽 아래 칸의 값을 반환
    return dist[N-1][N-1]

ans = [] # 각 테스트 케이스의 답을 넣을 리스트
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 배열
while True:
    N = int(input()) # 동굴의 크기
    if not N: break # 0이면 종료

    # 동굴의 각 칸에 있는 도둑루피의 크기
    cave = [list(map(int,input().split())) for _ in range(N)]

    # 제일 오른쪽 아래 칸까지 이동하면서 잃는 소지금의 최솟값을 리스트에 넣기
    ans.append(dijkstra())

# 각 테스트 케이스마다 정답 형식에 맞게 출력
for i in range(len(ans)):
    print(f'Problem {i+1}: {ans[i]}')
# 경로 찾기
# 그래프 이론, 그래프 탐색, 플로이드-와샬


N = int(input()) # 가중치 없는 방향 그래프 G의 정점 개수
adj = [list(map(int,input().split())) for _ in range(N)] # 인접 행렬

### 1. 플로이드-와샬
# 노드 k를 거치는 i->j 경로가 있는지 확인
for k in range(N):
    for i in range(N):
        # i와 k가 연결돼있지 않다면 경로가 없는 것이므로 다음 i를 탐색
        if not adj[i][k]: continue
        for j in range(N):
            # i와 j가 아직 연결돼있지 않고, k와 j는 연결돼있는 경우
            if not adj[i][j] and adj[k][j]:
                adj[i][j] = 1 # i->j 경로가 존재한다고 변경

# 모든 정점이 각각의 정점으로 가는 경로의 존재 여부를 인접 행렬 형식으로 출력
for row in adj:
    print(*row)

### 2. 행렬 곱을 활용한 풀이
# # adj를 곱하는 함수
# def mul(adj):
#     arr = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if adj[i][j]:
#                 arr[i][j] = 1
#                 continue
#             for k in range(N):
#                 if adj[i][k]*adj[k][j]:
#                     arr[i][j] = 1
#                     break
#     return arr

# # 정점 개수만큼 행렬 곱셈 반복
# # 행렬을 곱한 결과 값이 0보다 큰 경우 i->j 간선이 존재함
# for _ in range(N):
#     adj = mul(adj)

# # 모든 정점이 각각의 정점으로 가는 경로의 존재 여부를 인접 행렬 형식으로 출력
# for row in adj:
#     print(*row)
# 숨바꼭질 3
# 그래프와 BFS
# 1697. 숨바꼭질과 비슷
# 순간이동하는 경우를 먼저 고려하지 않을 경우,
# 앞의 경우에서 이미 visited를 갱신하여 1초 더 큰 값이 저장됨

from collections import deque

N,K = map(int,input().split())
q = deque([(N,0)])
visited = [-1]*100001 # 각 위치까지 가는 데 걸리는 최단 시간 저장, 아직 방문하지 않은 경우는 -1
visited[N] = 0
while q:
    cur,t = q.popleft()
    if cur == K: break
    if 2*cur < 100001 and abs(K-2*cur) <= abs(K-cur) and visited[2*cur]==-1:
        visited[2*cur] = t
        q.appendleft((2*cur,t)) # 순간이동은 0초 걸리므로 q의 맨 앞에 넣음
    if cur > 0 and visited[cur-1]==-1:
        visited[cur-1] = t+1
        q.append((cur-1,t+1))
    if cur < 100000 and visited[cur+1]==-1:
        visited[cur+1] = t+1
        q.append((cur+1,t+1))
print(visited[K])
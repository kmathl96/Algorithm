# 숨바꼭질
# 그래프와 BFS

from collections import deque

N,K = map(int,input().split())
q = deque([(N,0)]) # 위치와 시간
visited = [0]*100001 # 해당 위치에 가는 데 걸리는 최단 시간 저장 및 중복 방문 제거
while q:
    cur,t = q.popleft()
    if cur == K: break
    if cur > 0 and not visited[cur-1]:
        visited[cur-1] = t+1
        q.append((cur-1,t+1))
    if cur < 100000 and not visited[cur+1]:
        visited[cur+1] = t+1
        q.append((cur+1,t+1))
    # 순간이동한 위치가 현재 위치보다 도착점과 가까운 경우, 순간이동
    if 2*cur < 100001 and abs(K-2*cur) <= abs(K-cur) and not visited[2*cur]:
        visited[2*cur] = t+1
        q.append((2*cur,t+1))
print(visited[K])
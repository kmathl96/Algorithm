# 이모티콘
# 그래프와 BFS
# 방문 배열로 중복 제거를 하지 않을 경우 메모리 초과
# 화면의 이모티콘 개수(n)와 클립보드의 이모티콘 개수(copy)의 경우가 이미 있었는지 확인 

from collections import deque

S = int(input())
q = deque([(1,0,0)]) # (화면의 이모티콘 개수, 클립보드의 이모티콘 개수, 만드는 데 걸린 시간)
visited = [[0]*(S+1) for _ in range(S+1)]
while q:
    n,copy,d = q.popleft()
    if n==S: break # 화면의 이모티콘 개수와 S가 같을 경우, d가 최솟값을 가짐
    if n <= S and not visited[n][n]: # 1. 화면의 이모티콘을 복사
        q.append((n,n,d+1))
        visited[n][n] = 1
    if copy and S >= n+copy and not visited[n+copy][copy]: # 2. 클립보드의 이모티콘 붙여넣기
        q.append((n+copy,copy,d+1))
        visited[n+copy][copy] = 1
    if n > 1 and not visited[n-1][copy]: # 3. 화면의 이모티콘 중 하나 삭제
        q.append((n-1,copy,d+1))
        visited[n-1][copy] = 1
print(d)
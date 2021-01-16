# 이분 그래프
# 그래프와 BFS

from collections import deque

def bfs(v):
    q.append(v)
    arr[v] = 1
    while q:
        cur = q.popleft()
        for i in adj[cur]: # 현재 정점과 인접한 정점들
            if not arr[i]: # 아직 어느 집합에 들어가있지 않은 경우
                arr[i] = -arr[cur] # 현재 정점과 반대 집합
                q.append(i)
            elif arr[i] == arr[cur]: return 1 # 이미 현재 정점과 같은 집합에 존재함 = 이분 그래프 X
    return 0

for _ in range(int(input())):
    V,E = map(int,input().split())

    # 인접 리스트를 (V+1)*(V+1)로 만든 후 0/1로 표시하면 메모리 초과
    # 입력마다 해당 정점들을 삽입하는 방식으로 만들기
    adj = [[] for _ in range(V+1)]
    for e in range(E):
        v1,v2 = map(int,input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    arr = [0]*(V+1) # 1과 -1로 두 집합을 구분, 아직 집합에 들어가지 않은 경우는 0
    ans = 'YES'
    q = deque()
    for v in range(1,V):
        if not arr[v] and bfs(v): # 이분 그래프가 아닐 경우 ans 값 변경 후 종료
            ans = 'NO'
            break
    print(ans)
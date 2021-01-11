# ABCDE
# 그래프와 BFS
# adj 행렬을 N*N 크기로 만들어서 0과 1로 연결 여부를 나타내는 방식은 시간 초과
# adj를 빈 리스트들의 리스트로 초기화해놓고, 해당 정점과 연결돼 있는 정점을 그 리스트에 추가하는 방식으로

def f(cur,cnt):
    global flag
    if cnt == 5: # 5개가 이어져있을 경우 리턴
        flag = 1
        return
    for i in adj[cur]:
        if not visited[i]:
            visited[i] = 1
            f(i,cnt+1)
            visited[i] = 0

N,M = map(int,input().split())
adj = [[] for _ in range(N)] # 각 정점마다 연결되어있는 정점들
for i in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0]*N
flag = 0 # 5개의 정점이 연결돼있는지 여부 판단
for j in range(N): # 각 정점에서 시작
    visited[j] = 1
    f(j,1)
    if flag: break
    visited[j] = 0
print(flag)
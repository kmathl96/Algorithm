# 게리맨더링
# 그래프, 브루트포스

# 연결돼 있으면 인구 수 합 반환, 연결돼 있지 않으면 0 반환
def isConnected(group):
    st = [group[0]]
    visited = [0]*(N+1)
    visited[group[0]] = 1
    sum_ = population[group[0]-1]
    while st:
        s = st.pop()
        for v in group:
            if not visited[v] and adj[s][v]: # 방문한 적 없고 해당 구역과 인접한 구역
                st.append(v)
                visited[v] = 1
                sum_ += population[v-1]
    return sum_ if sum(visited)==len(group) else 0 # 모두 방문한 경우 = 연결돼 있음

N = int(input())
population = list(map(int,input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
ans = 1000

# 인접 행렬
for v in range(1,N+1):
    arr = list(map(int,input().split()))
    for i in arr[1:]:
        if not adj[v][i]: adj[v][i] = 1
        if not adj[i][v]: adj[i][v] = 1

# 두 선거구로 나누는 모든 경우
for i in range(1,1<<N-1):
    group1,group2 = [],[]
    for j in range(1,N+1):
        if i&1: group1.append(j)
        else: group2.append(j)
        i //= 2
    sum1,sum2 = isConnected(group1),isConnected(group2)
    if sum1 and sum2: # 두 선거구 다 isConnected 함수 반환 값이 0이 아닐 경우
        ans = min(ans, abs(sum1-sum2))
print(-1 if ans==1000 else ans)
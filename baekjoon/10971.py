# 외판원 순회 2
# 브루트 포스
# TSP(Traveling Salesman Problem)

N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*N # 방문 여부 체크
st = [(0,visited,0,1)] # 어디서 시작해도 상관 없음 => 0에서 시작
ans = 10000000
while st:
    cur,v,val,cnt = st.pop() # 현재 위치, visited, 현재까지의 비용 합, 이동 횟수
    if cnt == N:
        # 현재 위치에서 출발점(0)으로 돌아오는 길이 있을 경우
        # 그 비용을 합하여 최소값인지 비교
        if W[cur][0]: ans = min(ans, val+W[cur][0])
        continue
    for i in range(1,N):
        # 비용이 0이 아니며, 방문한 적 없고, 비용을 더해도 현재 답보다 작을 경우 방문
        if W[cur][i] and not v[i] and val+W[cur][i] < ans:
            v[i] = 1
            st.append((i,v[:],val+W[cur][i],cnt+1))
            v[i] = 0
print(ans)
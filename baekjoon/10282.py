# 해킹
# 다익스트라

import sys,heapq
input = sys.stdin.readline

def dijkstra(start):
    dist = [10000000]*(n+1) # 감염되기까지 걸리는 시간
    dist[start] = 0 # 처음 해킹당한 컴퓨터는 0초
    q = [(0,start)] # 최소 힙 : (감염 시간, 컴퓨터 번호)
    while q:
        t,cur = heapq.heappop(q)

        # 저장된 감염 시간보다 크다면 더 갱신할 필요가 없으므로 넘어감
        if dist[cur] < t: continue

        # 해당 컴퓨터를 의존하는 컴퓨터 탐색
        for node,sec in dep[cur]:
            # 해당 컴퓨터에 의해 감염되는 것이 더 빠른 경우
            if t+sec < dist[node]:
                dist[node] = t+sec # 감염 시간 변경
                heapq.heappush(q,(t+sec,node)) # 힙에 넣기
    return dist

# 입력된 테스트 케이스의 개수만큼 반복해서 결과를 리스트에 넣기
answer = []
for _ in range(int(input())):
    n,d,c = map(int,input().split()) # 컴퓨터 개수, 의존성 개수, 해킹 당한 컴퓨터의 번호
    
    # 의존성 저장
    dep = [[] for _ in range(n+1)]
    for _ in range(d):
        # 컴퓨터 a가 컴퓨터 b를 의존 (컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨)
        a,b,s = map(int,input().split())
        dep[b].append((a,s))
    
    # 감염된 컴퓨터 정보 구하기
    ans = [t for t in dijkstra(c) if t<10000000] # 감염된 컴퓨터들의 감염되기까지 걸린 시간
    answer.append([len(ans),max(ans)]) # 감염되는 컴퓨터의 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간

# 결과를 하나씩 출력
for ans in answer: print(*ans)
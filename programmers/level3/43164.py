# 여행경로
# 깊이/너비 우선 탐색(DFS/BFS)

def solution(tickets):
    N = len(tickets) # 티켓 개수

    # 티켓을 이름 기준 내림차순으로 정렬
    # 알파벳 순서가 앞서는 경로를 반환해야 하고, DFS는 LIFO 방식이므로 내림차순으로 정렬
    tickets.sort(reverse=1)

    # DFS
    visited = [0]*N # 각 티켓을 사용했는지 여부
    st = [(['ICN'],visited)] # 스택 초기화 : "ICN" 공항에서 출발
    while st:
        cur_path,visited = st.pop() # 현재까지의 방문 경로, 티켓 사용 여부 리스트
        # (티켓 수+1)개의 나라를 여행(= 모든 티켓을 사용)한 경우 해당 경로 반환
        if len(cur_path)==N+1: return cur_path

        # 티켓들 순회하면서 조건을 만족하면 스택에 넣기
        for i in range(N):
            s,e = tickets[i] # 해당 티켓의 출발지, 도착지

            # 현재 위치와 출발지가 다르거나, 이미 사용한 티켓인 경우 넘어감
            if cur_path[-1] != s or visited[i]: continue
            
            # 경로와 사용 여부 리스트를 갱신하여 스택에 넣기
            visited[i] = 1
            st.append((cur_path+[e],visited[:]))
            visited[i] = 0 # 원래대로 돌려놓기

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
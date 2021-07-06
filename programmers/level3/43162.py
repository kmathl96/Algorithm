# 네트워크
# 깊이/너비 우선 탐색(DFS/BFS)
    
def solution(n, computers):
    answer = 0 # 네트워크의 개수
    visited = [0]*n # 확인한 컴퓨터
    st = [] # 스택
    for com in range(n): # 모든 컴퓨터를 확인
        # DFS
        if visited[com]: continue # 이미 연결된 것을 확인한 컴퓨터는 넘어감
        st.append(com) # 스택에 넣음
        while st:
            cur = st.pop()
            visited[cur] = 1 # 해당 컴퓨터 확인
            for i in range(n): # 다른 컴퓨터와 연결돼 있는지 확인
                # 아직 확인하지 않았고, 해당 컴퓨터와 연결돼 있는 컴퓨터이면 스택에 넣기
                if not visited[i] and computers[cur][i]: st.append(i)
        answer += 1 # 네트워크 개수 갱신
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
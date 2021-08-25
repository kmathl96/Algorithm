# 물통
# DFS

A,B,C = map(int,input().split()) # 세 물통의 부피
answer = [] # 첫 번째 물통이 비어 있을 때, 세 번째 물통에 담겨있을 수 있는 물의 양
st = [(0,0,C)] # 스택 : 세 물통에 담긴 물의 양 (처음에는 세 번째 물통만 가득 차있음)

# 중복으로 스택에 넣지 않도록 체크해줌
# 전체 물의 양은 일정하므로, 1~2번째 물통만 체크 (세 번째 물통엔 나머지 물이 들어감)
visited = [[0]*(B+1) for i in range(A+1)]

while st:
    a,b,c = st.pop() # 세 물통에 들어있는 물의 양
    if visited[a][b]: continue # 이미 체크한 경우, 넘어감
    visited[a][b] = 1

    # 첫 번째 물통이 비어 있는 경우
    if not a:
        # 세 번째 물통의 물의 양을 answer에 넣음
        if c not in answer: answer.append(c)
    # 첫 번째 물통에 물이 있는 경우
    else:
        # 두 번째 물통에 물 붓기
        water = min(a,B-b)
        st.append((a-water,b+water,c))
        # 세 번째 물통에 물 붓기
        water = min(a,C-c)
        st.append((a-water,b,c+water))
    # 두 번째 물통에 물이 있는 경우
    if b:
        # 첫 번째 물통에 물 붓기
        water = min(b,A-a)
        st.append((a+water,b-water,c))
        # 세 번째 물통에 물 붓기
        water = min(b,C-c)
        st.append((a,b-water,c+water))
    # 세 번째 물통에 물이 있는 경우
    if c:
        # 첫 번째 물통에 물 붓기
        water = min(c,A-a)
        st.append((a+water,b,c-water))
        # 두 번째 물통에 물 붓기
        water = min(c,B-b)
        st.append((a,b+water,c-water))
print(*sorted(answer)) # 오름차순으로 정렬하여 출력
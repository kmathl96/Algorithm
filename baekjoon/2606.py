# 바이러스
# DFS

N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결되어 있는 컴퓨터 쌍의 수

# 각 컴퓨터와 연결된 컴퓨터를 리스트로 만들기
connected = [[] for _ in range(N+1)]
for _ in range(M):
    com1,com2 = map(int,input().split()) # 컴퓨터1, 컴퓨터2
    connected[com1].append(com2) # 컴퓨터1과 연결된 컴퓨터 리스트에 컴퓨터2 넣기
    connected[com2].append(com1) # 컴퓨터2와 연결된 컴퓨터 리스트에 컴퓨터1 넣기

# DFS로 확인
st = [1] # 스택 : 1번 컴퓨터를 넣음
checked = [0]*(N+1) # 확인 여부
checked[1] = 1 # 1번 확인
ans = 0 # 웜 바이러스에 걸리게 되는 컴퓨터의 수
while st:
    cur = st.pop() # 현재 컴퓨터
    for com in connected[cur]: # 현재 컴퓨터와 연결되어 있는 컴퓨터들
        if checked[com]: continue # 이미 확인한 경우 넘어감
        st.append(com) # 스택에 넣기
        checked[com] = 1 # 확인
        ans += 1 # 바이러스에 걸린 컴퓨터 수 추가
print(ans)
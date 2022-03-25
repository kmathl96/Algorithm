# 촌수계산
# DFS

n = int(input()) # 전체 사람의 수
num1,num2 = map(int,input().split()) # 촌수를 계산해야 하는 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수
adj = [[0]*(n+1) for _ in range(n+1)] # 인접 행렬
for _ in range(m):
    x,y = map(int,input().split()) # 부모와 자식의 번호
    adj[x][y],adj[y][x] = 1,1 # 서로 인접하므로 체크
ans = -1
st = [(num1,0)] # 스택
visited = [0]*(n+1) # 방문 배열
visited[num1] = 1
while st:
    num,d = st.pop() # 현재 사람의 번호, num1과의 촌수
    
    # 현재 사람이 num2인 경우, 종료
    if num==num2:
        ans = d # 촌수 저장
        break

    for i in range(1,n+1):
        # 인접하고 아직 확인한 적 없는 사람인 경우
        if adj[num][i] and not visited[i]:
            st.append((i,d+1)) # 더 탐색하기 위해 스택에 넣기
            visited[i] = 1 # 방문 체크
print(ans)
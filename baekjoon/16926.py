# 배열 돌리기 1
# 구현

from collections import deque

N,M,R = map(int,input().split()) # 배열의 크기와 수행해야 하는 회전의 수
arr = [list(input().split()) for _ in range(N)] # 배열의 원소
dr,dc = [0,1,0,-1],[1,0,-1,0] # 방향
q = deque() # 배열의 테두리를 큐에 넣고 rotate 수행
d = 0 # 큐에 넣을 원소를 탐색할 방향

# N, M 중 작은 값을 반으로 나눈 만큼(= 테두리의 개수) 반복
for i in range(min(N,M)//2):
    r,c = i,i # 테두리의 시작점(왼쪽 상단)

    # 테두리를 구성하는 요소의 개수만큼 큐에 넣기
    for _ in range(2*(N-2*i-1)+2*(M-2*i-1)):
        q.append(arr[r][c]) # 큐에 넣기
        r,c = r+dr[d],c+dc[d] # 다음 위치로 갱신
        
        # 테두리의 꼭짓점인 경우 방향 변경
        if r in (i,N-1-i) and c in (i,M-1-i): d = (d+1)%4
    
    # 반시계 방향으로 돌리기
    # 테두리의 길이로 나눈 나머지만큼 돌리는 것과 같음
    q.rotate(-R%len(q))

    # 큐의 원소들을 순서대로 다시 배열에 저장
    while q:
        arr[r][c] = q.popleft()
        r,c = r+dr[d],c+dc[d]
        if r in (i,N-1-i) and c in (i,M-1-i): d = (d+1)%4

# 배열을 회전 시킨 결과를 출력
for row in arr:
    print(*row)
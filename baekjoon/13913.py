# 숨바꼭질 4
# BFS
# 경로를 큐에 같이 넣으면 메모리 초과 발생
#  => 각 점의 이동 위치를 저장하여 나중에 경로 계산

from collections import deque

# 마지막 위치(pos)에서부터 이전 위치로 되돌아가며 경로 저장
def path(pos,t):
    temp = [pos] # 마지막 위치
    for _ in range(t):
        pos = pre_visited[pos] # 이전 위치로 이동
        temp.append(pos)
    return reversed(temp) # 뒤집어서 반환

N,K = map(int,input().split()) # 수빈이와 동생의 위치
q = deque([(N,0)]) # 큐 : (현재 위치, 시간)
pre_visited = [-1]*100001 # 이전에 방문한 위치
while q:
    X,t = q.popleft() # 수빈이의 현재 위치, 현재 위치까지 오는 데 걸린 시간

    # 동생과 같은 위치인 경우, 동생을 찾은 것이므로 종료
    if X == K: break

    # 다음 위치로 이동
    for nxt in (X-1,X+1,X*2):
        # 유효한 위치이며 이전에 방문한 적 없는 경우 이동
        if 0<=nxt<=100000 and pre_visited[nxt]==-1:
            pre_visited[nxt] = X # nxt의 이전 위치는 X임을 저장
            q.append((nxt,t+1)) # 큐에 넣기

print(t) # 수빈이가 동생을 찾는 가장 빠른 시간
print(*path(X,t)) # 어떻게 이동해야 하는지 출력
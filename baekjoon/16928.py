# 뱀과 사다리 게임
# BFS

from collections import deque

N,M = map(int,input().split()) # 사다리의 수, 뱀의 수

# 각 칸에 도착 시 이동할 칸
# 사다리나 뱀이 없는 경우, 각 칸에 해당하는 숫자
board = list(range(101))
for _ in range(N+M):
    x,y = map(int,input().split()) # 사다리/뱀의 정보
    board[x] = y # x번 칸에 도착하면 y번 칸으로 이동

# 탐색
q = deque([(1,0)]) # 큐 : 1번 칸에서 시작
visited = [0]*101 # 방문 배열
visited[1] = 1 # 1번 칸 체크
while q:
    cur,d = q.popleft() # 현재 위치, 주사위를 굴린 횟수

    # 현재 위치가 94 이상인 경우, 주사위를 굴려서 100번 칸에 갈 수 있음
    if cur>=94:
        break # 더 탐색하지 않고 종료

    # 주사위를 굴려서 이동
    for nxt in range(cur+1,cur+7):
        # 100번 칸이 마지막이므로, 100을 넘어가면 종료
        if nxt > 100: break

        # 이미 방문한 경우, 재방문하지 않음
        if visited[nxt]: continue

        q.append((board[nxt],d+1)) # # 더 탐색하기 위에 큐에 넣기
        visited[nxt] = 1 # 방문 체크

# 주사위를 한 번 덜 굴린 상태에서 종료했으므로, 결과에 1 더한 값을 출력
print(d+1)
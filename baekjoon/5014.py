# 스타트링크
# BFS

from collections import deque

def sol():
    # F : 스타트링크 사무실이 있는 건물의 층수
    # S : 강호가 지금 있는 곳
    # G : 스타트링크가 있는 곳의 위치
    # U, D : 엘리베이터는 위로 U층, 아래로 D층을 가는 버튼 2개만 있음
    F,S,G,U,D = map(int,input().split())
    
    q = deque([(S,0)]) # 큐 : (현재 위치, 버튼 누른 횟수)
    visited = [0]*(F+1) # 방문 배열
    visited[S] = 1 # 시작점은 이미 방문했으므로 체크
    ans = 'use the stairs' # 갈 수 없는 경우 출력할 문자열로 초기화
    dirs = [U,-D] # 방향 배열
    while q:
        cur,cnt = q.popleft() # 현재 위치, 버튼 누른 횟수
        
        # G층에 도착한 경우, 횟수를 저장하고 종료
        if cur == G:
            ans = cnt
            break

        # 버튼을 눌러서 이동
        for d in dirs:
            # 유효한 층이며 아직 방문하지 않은 층인 경우
            if 1<=cur+d<=F and not visited[cur+d]:
                q.append((cur+d,cnt+1)) # 더 탐색하기 위해 큐에 넣기
                visited[cur+d] = 1 # 방문 체크
    print(ans)

sol()
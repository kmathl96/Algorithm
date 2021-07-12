# 거리두기 확인하기
# 2021 카카오 채용연계형 인턴십
# BFS

from collections import deque

dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 리스트

# 해당 대기실(place)의 (row,col)에 위치한 사람이 거리두기를 지키고 있는지 확인
def correct(row,col,place):
    q = deque([(row,col,0)])
    visited = [[0]*5 for _ in range(5)] # 확인했는지 체크하기 위한 리스트
    while q:
        r,c,d = q.popleft()
        visited[r][c] = 1
        if d==2: break # 거리가 2를 넘는 자리는 더 확인할 필요 없으므로 종료
        for i in range(4): # 사방 탐색
            nr,nc = r+dr[i],c+dc[i] # 탐색할 위치
            # 유효한 위치이며, 아직 방문하지 않은 경우
            if 0<=nr<5 and 0<=nc<5 and not visited[nr][nc]:
                # 빈 테이블인 경우, 그 자리에서 또 탐색하기 위해 q에 넣기
                if place[nr][nc] == 'O': q.append((nr,nc,d+1))
                # 응시자가 앉아있는 경우, 거리두기를 지키지 않은 것이므로 0 반환
                elif place[nr][nc] == 'P': return 0
    return 1 # 한번도 거리두기를 지키지 않은 경우가 없었다면, 1 반환

def solution(places):
    answer = [] # 거리두기 준수 여부를 담을 리스트
    
    # 각 대기실에서 거리두기를 준수하고 있는지 확인
    for place in places:
        place = [list(s) for s in place] # 문자열을 리스트로 만듦
        flag = 1 # 거리두기 준수 여부
        for r in range(5):
            for c in range(5):
                # 해당 자리가에 응시자가 있고, 거리두기를 지키지 않은 경우
                if place[r][c] == 'P' and not correct(r,c,place):
                    flag = 0 # 거리두기 준수 여부 변경 후 종료
                    break
            if not flag: break # 거리두기 준수를 한 명이라도 하지 않은 경우 종료
        answer.append(flag) # 거리두기 준수 여부 담기
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])) # [1, 0, 1, 1, 1]

print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]])) # [0]
print(solution([["OOPOO", "OOOOO", "OOOOO", "OOOOO", "OPOPO"]])) # [0]
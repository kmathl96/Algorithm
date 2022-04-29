# 나이트 투어
# 구현, 시뮬레이션

path = [input() for _ in range(36)] # 영식이의 나이트 투어 경로
visited = [[0]*6 for _ in range(6)] # 방문 배열
cur = ord(path[35][0])-65,int(path[35][1])-1 # 현재 위치 (마지막 순서의 좌표)
ans = 'Valid' # 나이트 투어 경로가 올바른지 여부

# 나이트 투어 경로 순서대로 확인
for s in path:
    r,c = ord(s[0])-65,int(s[1])-1 # 나이트가 이동할 위치

    # 이미 방문했거나, 나이트가 갈 수 없는 칸인 경우
    if visited[r][c] or (abs(cur[0]-r),abs(cur[1]-c)) not in ((1,2),(2,1)):
        ans = 'Invalid' # 올바르지 않음
        break # 더 탐색할 필요가 없으므로 종료
    
    # 나이트 이동
    visited[r][c] = 1 # 방문 표시
    cur = r,c # 현재 위치를 변경

print(ans)
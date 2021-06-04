# 방문 길이
# Summer/Winter Coding(~2018)
# 원래 문제에서는 좌표평면의 경계가 -5<=x<=5, -5<=y<=5로 주어져있는데,
# 방문 배열 처리를 쉽게 하기 위해 0<=x<=10, 0<=y<=10으로 처리할 것
# 좌표도 마찬가지로 문제에서의 위치 (x, y)보다 5씩 크게 처리

def solution(dirs):
    answer = 0 # 답 초기화
    cur = [5,5] # 현재 위치 : 원래 문제에서 (0,0)이었지만, 변경한 좌표평면에 맞게 (5,5)로 저장

    # 방문 배열 (중복 체크)
    # (x,y) 위치에서 오른쪽(x+1,y), 위쪽(x,y+1) 방향으로 가는 경로를 방문했는지 여부
    visited = [[[0,0] for _ in range(10)] for i in range(10)]

    for d in dirs:
        x,y = cur # 현재 위치
        if d == 'U' and 0<=x<=10 and 0<=y+1<=10: # 해당 방향으로 갔을 때 유효한 위치이면 이동
            if not visited[x][y][1]: # 아직 지나치지 않은 경로인 경우
                visited[x][y][1] = 1 # 방문 체크
                answer += 1 # 답 갱신
            cur[1] += 1 # 현재 위치 갱신
        elif d == 'D' and 0<=x<=10 and 0<=y-1<=10:
            if not visited[x][y-1][1]:
                visited[x][y-1][1] = 1
                answer += 1
            cur[1] -= 1
        elif d == 'L' and 0<=x-1<=10 and 0<=y<=10:
            if not visited[x-1][y][0]:
                visited[x-1][y][0] = 1
                answer += 1
            cur[0] -= 1
        elif d == 'R' and 0<=x+1<=10 and 0<=y<=10:
            if not visited[x][y][0]:
                visited[x][y][0] = 1
                answer += 1
            cur[0] += 1
    return answer

print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7
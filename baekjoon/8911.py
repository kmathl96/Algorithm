# 거북이
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

# 거북이 로봇의 방향
# 순서대로 북쪽-동쪽-남쪽-서쪽을 쳐다봄
dr,dc = [-1,0,1,0],[0,1,0,-1]

# 테스트 케이스의 개수만큼 반복
for _ in range(int(input())):
    x,y,d = 0,0,0 # 거북이의 위치와 방향

    # 거북이가 지나간 영역의 x, y 좌표의 최솟값과 최댓값을 각각 min_x, max_x, min_y, max_y라고 할 때,
    # 해당 영역을 모두 포함할 수 있는 가장 작은 직사각형은
    # 네 점 (min_x,min_y), (min_x,max_y), (max_x,min_y), (max_x,max_y)로 이루어짐
    # 이 직사각형의 넓이는 (max_x - min_x) * (max_y - min_y)
    # 처음에 (0,0)에 있으므로 각각 0으로 초기화
    min_x,min_y,max_x,max_y = 0,0,0,0

    # 컨트롤 프로그램의 명령을 순서대로 실행
    for cmd in input():
        # 1. F: 한 눈금 앞으로
        if cmd == 'F':
            x += dr[d]
            y += dc[d]
        # 2. B: 한 눈금 뒤로
        elif cmd == 'B':
            x -= dr[d]
            y -= dc[d]
        # 3. L: 왼쪽으로 90도 회전
        elif cmd == 'L':
            d = (d-1)%4
        # 4. R: 오른쪾으로 90도 회전
        else:
            d = (d+1)%4
        
        # x, y 각각의 최솟값과 최댓값 갱신
        if min_x > x: min_x = x
        elif max_x < x: max_x = x
        if min_y > y: min_y = y
        elif max_y < y: max_y = y
    
    # 직사각형의 넓이 출력
    print((max_x-min_x)*(max_y-min_y))
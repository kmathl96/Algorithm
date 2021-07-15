# 컨베이어 벨트 위의 로봇
# 구현, 시뮬레이션

N,K = map(int,input().split()) # N : 컨베이어 벨트의 길이
belt = list(map(int,input().split())) # 벨트 각 칸의 내구도
robot = [0]*N # 윗 벨트의 각 칸에 로봇이 있는지 여부
cnt0,ans = 0,0 # 내구도가 0인 칸의 개수, 단계 수

# 로봇 옮기기
while cnt0 < K: # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 종료
    ans += 1 # 단계 갱신
    
    # 1. 벨트 회전
    belt.insert(0,belt.pop()) # 벨트 회전
    robot.insert(0,robot.pop()) # 로봇도 같이 회전
    robot[-1] = 0 # N번 칸의 로봇 내리기

    # 2. 로봇 이동
    for i in range(N-2,0,-1): # 먼저 벨트에 올라간 로봇부터 이동
        # 해당 칸에 로봇이 있고, 이동하려는 칸(다음 칸)에 로봇이 없으며,
        # 그 칸의 내구도가 1 이상이어야 함
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i],robot[i+1] = 0,1 # 해당 칸과 다음 칸의 로봇 존재 여부 변경
            belt[i+1] -= 1 # 다음 칸의 벨트 내구도 감소
            if not belt[i+1]: cnt0 += 1 # 0이 되면 cnt0(0의 개수) 증가
    robot[-1] = 0 # 이동 후 N번 칸에 있는 로봇 내리기
    
    # 3. 로봇 올리기
    if belt[0]: # 올리는 위치에 있는 칸의 내구도가 0이 아닌 경우
        robot[0] = 1 # 로봇 올리기
        belt[0] -= 1 # 해당 칸의 내구도 감소
        if not belt[0]: cnt0 += 1 # 내구도가 0이 되면 cnt0(0의 개수) 증가
print(ans)
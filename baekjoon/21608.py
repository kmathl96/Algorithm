# 상어 초등학교
# 구현

N = int(input()) # N*N 크기의 교실
room = [[0]*N for _ in range(N)] # 빈 교실
like_student = {} # 각 학생이 좋아하는 학생들을 저장할 딕셔너리
dr,dc = [-1,0,1,0],[0,1,0,-1] # 방향 리스트
for _ in range(N**2):
    info = list(map(int,input().split())) # 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호
    students = set(info[1:]) # 좋아하는 학생 4명의 번호
    like_student[info[0]] = students # 딕셔너리에 저장
    choose = [0,0,0,0] # 선택할 자리의 좌표, 그 자리에서의 좋아하는 학생 수와 빈 자리 수
    first_empty = 0 # 모든 자리를 확인했으나 적절한 자리를 못 찾은 경우 선택할 빈 자리
    for r in range(N):
        for c in range(N):
            if room[r][c]: continue # 이미 앉은 자리라면 넘어감

            # 모든 자리를 확인하면서 처음 나온 빈 자리를 저장
            # 좋아하는 학생이 아직 자리를 정하지 않아 적절한 자리를 못 찾은 경우, 이 자리를 선택
            if not first_empty: first_empty = (r,c)

            # 인접한 자리 확인
            like,empty = 0,0 # 인접한 칸에 있는 좋아하는 학생 수와 빈 자리의 수
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i] # 확인할 자리
                if 0<=nr<N and 0<=nc<N:
                    if not room[nr][nc]: empty += 1 # 비어있다면 empty 증가
                    elif room[nr][nc] in students: like += 1 # 좋아하는 학생인 경우 like 증가
            
            # 선택된 자리보다 좋아하는 학생 수가 더 크거나, 좋아하는 학생 수가 같고 빈 자리 수가 더 큰 경우
            if choose[2] < like or (choose[2] == like and choose[3] < empty):
                choose = [r,c,like,empty] # 선택할 자리 변경
    
    # 선택된 자리의 좌표가 (0,0)이라면, 처음 발견한 빈 자리로 변경 
    if not choose[0] and not choose[1]: choose[0],choose[1] = first_empty
    room[choose[0]][choose[1]] = info[0] # 선택한 자리를 학생 번호로 변경

# 모든 학생들의 만족도 구하기
ans = 0 # 만족도의 총 합
for r in range(N):
    for c in range(N):
        cnt = 0 # 좋아하는 학생 수
        likes = like_student[room[r][c]] # 해당 자리에 앉은 학생이 좋아하는 학생들
        
        # 인접한 자리를 확인하여, 좋아하는 학생인 경우 cnt 증가
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<N and 0<=nc<N and room[nr][nc] in likes: cnt += 1
        
        # 만족도를 계산하여 총합에 더하긴
        # 0이면 0
        # 1이면 1, 2이면 10, 4이면 1000 => 10^(cnt-1)
        ans += 10**(cnt-1) if cnt else 0
print(ans)
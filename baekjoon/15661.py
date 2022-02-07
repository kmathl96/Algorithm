# 링크와 스타트
# 브루트포스

N = int(input()) # 축구를 하기 위해 모인 사람의 수

# S[i][j] = i번 사람과 j번 사람이 같은 팀에 속했을 때 팀에 더해지는 능력치
S = [list(map(int,input().split())) for _ in range(N)]

ans = 2000 # 두 팀의 능력치의 차이의 최솟값

# 경우를 비트로 생각하면,
# 00...01부터 (팀 인원 수는 한 명 이상이어야 함)
# 01...11까지 탐색 (이후 비트는 앞에 이미 해당 비트를 뒤집은 경우(결과 같음)가 있으므로 고려할 필요가 없음)
# ex) 1,2번 사람이 스타트 팀, 3,4번 사람이 링크 팀인 경우(0011)와 각자 반대의 팀이 되는 경우(1100)의 능력치 차이는 같음
for case in range(1,1<<N-1):
    # 팀 나누기
    start = [0]*N # 스타트 팀의 인원 여부
    for j in range(N):
        if case&1: start[j] = 1
        case //= 2
    
    # 능력치 차이 구하기
    diff = 0 # 능력치 차이
    for i in range(N-1):
        for j in range(i+1,N):
            # 스타트 팀인 경우 더하기
            if start[i] and start[j]:
                diff += S[i][j]+S[j][i]
            # 링크 팀인 경우 빼기
            elif not start[i] and not start[j]:
                diff -= S[i][j]+S[j][i]
    ans = min(ans,abs(diff)) # 최솟값으로 갱신
    if ans==0: break # 0이면 더 탐색할 필요가 없으므로 종료
print(ans)
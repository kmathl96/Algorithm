# 월드컵
# 브루트포스, 백트래킹

# team1과 team2의 결과를 비교하여 계산
def f(team1,team2):
    global flag

    # 이미 가능한 조합을 찾은 경우, 더 탐색하지 않고 종료
    if flag: return

    # 마지막까지 탐색했다면 가능한 것이므로 종료
    if team2 == 6:
        flag = 1
        return
    
    # 승-패, 무-무, 패-승 순서대로 계산
    for i in range(3):
        # 각각의 수가 1 이상이면 가능
        if result[team1*3+i] and result[team2*3+2-i]:
            # 각 수를 감소시킴
            result[team1*3+i] -= 1
            result[team2*3+2-i] -= 1
            
            # 2번째 팀이 마지막 팀이 아니라면 1번째 팀과 그다음 팀 비교
            if team2 < 5: f(team1,team2+1)
            # 마지막 팀인 경우, 1번째 팀의 다음 팀과 다다음 팀
            else: f(team1+1,team1+2)
            
            # 각 수를 다시 증가시켜서 원래 상태로 돌림
            result[team1*3+i] += 1
            result[team2*3+2-i] += 1

answer = [] # 각각의 결과를 담을 리스트
for i in range(4):
    result = list(map(int,input().split())) # 결과
    flag = 1 # 결과의 가능(1)/불가능(0) 여부

    # 우선 여섯 팀의 승, 무승부, 패의 수의 합이 5여야 함
    for i in range(6):
        # 합이 5가 안 되는 팀이 있는 경우, 결과는 불가능하므로 종료
        if sum(result[i*3:i*3+3]) != 5:
            flag = 0
            break
    
    # 위에서 확인했을 때 가능하다면, 팀끼리 비교해서 확인
    # (불가능하다면 더 탐색할 필요가 없기 때문)
    if flag:
        flag = 0
        f(0,1) # 0번 팀과 1번 팀부터 비교
    
    answer.append(flag) # 결과를 저장
print(*answer)
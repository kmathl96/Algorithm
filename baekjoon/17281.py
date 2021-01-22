# ⚾
# 브루트포스

from itertools import permutations

N = int(input())
innings = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for p in permutations(range(1,9)): # 2~9번 선수들로 타순 만듦
    players = list(p)
    players.insert(3,0) # 해당 타순에 1번 선수를 3번 타자로 삽입
    score = 0
    hitter = 0 # 1번 타자부터 시작, 이닝이 바뀌어도 유지되므로 이닝 시작 전에 초기화
    for inning in innings:
        out = 0 # 3 아웃 되면 다음 이닝으로 넘어감
        b1,b2,b3 = 0,0,0 # 3~1루에 타자가 있는지 여부
        while out < 3: # 3 아웃 되기 전까지 반복
            hit = inning[players[hitter]] # 결과 => 진루의 개수
            # 다음 타자로 변경
            hitter += 1
            if hitter > 8: hitter = 0
            # 아웃일 경우 진루하지 않음
            if not hit:
                out += 1
                continue
            # 안타/홈런인 경우 진루
            score += b1 # 3루에 타자가 있다면 득점
            b1,b2,b3 = b2,b3,1 # 2, 1루수는 다음으로, 타자는 1루로 진루
            for _ in range(hit-1): # 타자가 지나간 루는 공석으로 채움
                score += b1 # 3루에 타자가 있다면 특점
                b1,b2,b3 = b2,b3,0 # 1루에 공석, 나머지 선수들 진루
    ans = max(ans, score)
print(ans)
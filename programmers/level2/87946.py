# 피로도
# 순열

from itertools import permutations

def solution(k, dungeons):
    answer = 0 # 유저가 탐험할 수 있는 최대 던전 수
    N = len(dungeons) # 던전의 개수

    for perm in permutations(range(N)):
        cur,cnt = k,0 # 현재 피로도, 탐험한 던전 수

        # 순서대로 던전 탐색
        for i in perm:
            # 최소 필요 피로도가 현재 피로도 이하인 경우, 던전 탐험
            if dungeons[i][0] <= cur:
                cnt += 1 # 탐험한 던전 수 증가
                cur -= dungeons[i][1] # 소모 피로도만금 피로도 하락
        
        if answer < cnt: answer = cnt # answer 갱신
    return answer

print(solution(80,[[80,20],[50,40],[30,10]])) # 3
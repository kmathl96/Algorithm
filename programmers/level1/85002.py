# 복서 정렬하기

def solution(weights, head2head):
    answer = []
    N = len(weights) # 복서 선수의 수
    for i in range(N):

        cnt = 0 # 자신보다 몸무게가 무거운 복서를 이긴 횟수
        for j in range(N):
            if head2head[i][j]=='W' and weights[i] < weights[j]: cnt += 1
        
        w,l = head2head[i].count('W'),head2head[i].count('L') # 이긴 횟수와 진 횟수
        answer.append((0 if w+l == 0 else w/(w+l),cnt,weights[i],i+1)) # 승률, 자신보다 무거운 복서를 이긴 횟수, 자기 몸무게, 번호
    
    # 승률, 이긴 횟수, 몸무게 기준 내림차순, 번호 기준 오름차순으로 정렬하여 번호 반환
    return [ans[3] for ans in sorted(answer, key=lambda x: (-x[0],-x[1],-x[2],x[3]))]

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])) # [3,4,1,2]
print(solution([145,92,86], ["NLW","WNL","LWN"])) # [2,3,1]
print(solution([60,70,60], ["NNN","NNN","NNN"])) # [2,1,3]
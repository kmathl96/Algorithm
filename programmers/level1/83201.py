# 상호 평가

def solution(scores):
    N = len(scores) # 학생 수
    answer = '' # 학생들의 학점

    # 유일한 최고점/최저점인지 쉽게 판단하기 위해 (max, min, sum 함수를 적용하기 위해)
    # score[i]를 i번 학생이 평가한 점수가 아니라, i번 학생이 받은 점수로 바꿈
    scores = [[scores[c][r] for c in range(N)] for r in range(N)]
    
    for i in range(N):
        # 본인을 평가한 점수, 본인이 받은 점수의 최저점/최고점과 총합
        n,mn,mx,sm = scores[i][i],min(scores[i]),max(scores[i]),sum(scores[i])
        
        # 평균 구하기
        # 유일한 최저점/최고점인 경우, 그 점수를 제외하고 평균을 구함
        if (n == mn and scores[i].count(mn) == 1) or (n == mx and scores[i].count(mx) == 1):
            avg = (sm-n)/(N-1)
        else: avg = sm/N

        # 평균에 따라 학점 부여
        if avg >= 90: answer += 'A'
        elif avg >= 80: answer += 'B'
        elif avg >= 70: answer += 'C'
        elif avg >= 50: answer += 'D'
        else: answer += 'F'
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])) # "FBABD"
print(solution([[50,90],[50,87]])) # "DA"
print(solution([[70,49,90],[68,50,38],[73,31,100]])) # "CFD"
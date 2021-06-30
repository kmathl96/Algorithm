# 순위 검색
# 2021 KAKAO BLIND RECRUITMENT

from itertools import combinations

# query의 모든 경우의 수
# 조건을 전부 이어붙여서 key를 만듦
# 데이터를 더 용이하게 처리하기 위해 '-'는 ''로 대체
# '', 'cpp', 'java', 'python', 'backend', 'cppbackend', 'javabackend', ... , 'javafrontendseniorpizza', 'pythonfrontendseniorpizza'
cases = {lang+job+career+food:[] for food in ('','chicken','pizza') for career in ('','junior','senior') for job in ('','backend','frontend') for lang in ('','cpp','java','python')}

def solution(info, query):
    answer = [] # 각 query의 조건을 만족하는 사람 수

    # 지원자의 점수를 cases에 넣음
    for i in info:
        i = i.split()
        for j in range(5):
            for comb in combinations(i[:4], j): # 개발언어, 직군, 경력, 소울푸드 중 0~4가지를 만족하는 경우
                cases[''.join(comb)].append(int(i[-1])) # 점수 넣기

    # 점수 오름차순 정렬
    for k in cases.keys():
        cases[k].sort()

    # 각 query의 조건을 만족하는 사람 수 확인
    for q in query:
        q = q.split()
        score = int(q[-1]) # 조건의 점수
        # 점수를 제외한 조건을 모두 이어붙임
        # ex) "- and backend and senior and - 150"
        #   => "-andbackendandseniorand-"
        #   => "-backendsenior-"
        #   => "backendsenior"
        q = ''.join(q[:-1]).replace('and', '').replace('-', '')
        scores = cases[q] # 해당 조건을 만족하는 점수들
        
        # 이진 탐색
        l,r = 0,len(scores) # 양 끝 index값
        while l<r:
            m = (l+r)//2 # 중간 index값
            # 조건 점수가 중간 값 이하인 경우, 오른쪽 index값 갱신
            if scores[m] >= score: r = m
            # 중간 값보다 큰 경우, 왼쪽 index값 갱신
            else: l = m+1
        answer.append(len(scores)-l) # answer 갱신
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query)) # [1,1,1,1,2,4]
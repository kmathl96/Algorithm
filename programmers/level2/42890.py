# 후보키
# 2019 KAKAO BLIND RECRUITMENT

from itertools import combinations

# 유일성 확인
def check_uniqueness(relation,case):
    db = set() # 튜플을 넣을 리스트
    for tp in relation: # 각 튜플
        # 각 튜플이 해당 속성의 데이터만 가지도록 처리
        data = []
        for c in case:
            data.append(tp[c])
        # 해당 튜플이 중복된다면 False 반환
        if tuple(data) in db: return False
        db.add(tuple(data)) # 중복되지 않은 경우 리스트에 넣기
    return True # 한번도 중복된 적이 없다면 유일성 만족

# 최소성 확인
def check_minimality(answer,case):
    # 더 적은 개수의 속성을 갖고 있는 후보키를 포함하고 있다면 최소성을 만족하지 못함
    for ans in answer: # 후보키 순회
        # 차집합이 공집합이면 (= 해당 후보키를 포함) False 반환
        if not (ans-case): return False
    return True

def solution(relation):
    answer = [] # 후보키를 저장할 리스트
    # 속성의 집합을 만드는 모든 경우를 구해서 순회
    for n in range(1,len(relation)+1): # 속성 n개로 구성
        for case in combinations(range(len(relation[0])),n):
            # 유일성과 최소성을 만족하는 경우 후보키이므로 answer에 넣음
            if check_uniqueness(relation, case) and check_minimality(answer,set(case)):
                answer.append(set(case))
    return len(answer) # 후보키의 개수

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])) # 2
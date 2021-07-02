# 메뉴 리뉴얼
# 2021 KAKAO BLIND RECRUITMENT

from itertools import combinations

def solution(orders, course):
    answer = [] # 새로 추가하게 될 코스요리의 메뉴 구성을 담을 리스트

    # 코스요리 메뉴 종류 개수에 맞게 코스요리 메뉴 구성을 구함
    for c in course:
        dic = {} # 각 코스요리 조합의 주문 횟수를 넣을 딕셔너리
        for order in orders:
            for comb in combinations(order, c): # 해당 메뉴 구성 중 c가지 메뉴 조합들
                # 메뉴 조합을 정렬하여 dic 갱신
                s = ''.join(sorted(comb))
                if s in dic.keys(): dic[s] += 1
                else: dic[s] = 1

        # 가장 많이 함께 주문한 메뉴 구성 찾기
        mx_cnt,mx_val = 0,[] # 최대 주문 횟수, mx_cnt만큼 주문된 메뉴 구성
        for k in dic.keys():
            cnt = dic[k] # 해당 메뉴 구성을 주문한 횟수
            if cnt < 2: continue # 최소 2명 이상의 손님으로부터 주문되어야 함
            if mx_cnt < cnt: # mx_cnt보다 큰 경우
                mx_cnt = cnt # mx_cnt 변경
                mx_val = [k] # mx_val 초기화하고 현재 메뉴 구성 넣기
            elif mx_cnt == cnt: mx_val.append(k) # mx_cnt와 같은 경우, mx_val에 넣기
        answer.extend(mx_val) # answer에 추가
    return sorted(answer) # 오름차순 정렬하여 반환

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])) # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4])) # ["WX", "XY"]
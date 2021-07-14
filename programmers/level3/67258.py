# 보석 쇼핑
# 2020 카카오 인턴십

### 1. dictionary를 활용한 풀이 ###
def solution(gems):
    N,M = len(gems),len(set(gems)) # 보석의 개수, 보석 종류의 개수
    answer = [1,N] # 최대 범위로 초기화
    cnt = {} # 해당 구간에 있는 보석의 개수

    s,e = 0,M # [s,e) 구간의 양 끝 index 값 (구간의 최소 길이는 보석 종류의 개수와 같음)
    # 현재 구간(0~M-1)에 있는 보석의 개수를 딕셔너리에 저장
    for i in range(e):
        gem = gems[i]
        if gem in cnt: cnt[gem] += 1 # 1개 추가
        else: cnt[gem] = 1 # 아직 없으면 1개로 저장
    
    # 유효한 범위 내에서 s나 e를 갱신하며 반복
    while s<=N-M and s<=e<=N:
        # 해당 구간의 보석 종류의 개수가 M인 경우 (= 모든 보석이 있음)
        # s를 1 증가시켜서 범위를 좁힘
        if len(cnt) == M:
            # 구간의 길이가 더 작다면 갱신
            if answer[1]-answer[0]+1 > e-s: answer = [s+1,e]
            cnt[gems[s]] -= 1 # 해당 보석의 개수 감소
            if not cnt[gems[s]]: del cnt[gems[s]] # 개수가 0이 되면 제거
            s += 1 # index 갱신
        else: # 적은 경우, e를 1 증가시켜서 범위를 넓힘
            if e == N: break # 끝인 경우 종료
            if gems[e] in cnt: cnt[gems[e]] += 1 # 해당 보석의 개수 증가
            else: cnt[gems[e]] = 1 # cnt에 없는 경우, 1로 저장
            e += 1 # index 갱신
    return answer

### 2. list slicing을 활용한 풀이 (시간 초과) ###
# def solution(gems):
#     N,M = len(gems),len(set(gems))
#     answer = [1,N]
#     s,e = 0,M
#     while s<=N-M and s<=e<=N:
#         cnt = len(set(gems[s:e]))
#         if cnt == M:
#             if answer[1]-answer[0]+1 > e-s: answer = [s+1,e]
#             s += 1
#         elif e == N: s += 1
#         else: e += 1
#     return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]

print(solution(["A","A","A","B","B"])) # [3, 4]
print(solution(["A"])) # [1, 1]
print(solution(["A","B","B","B","B","B","B","C","B","A"])) # [8, 10]
# 신고 결과 받기

def solution(id_list, report, k):
    answer = [0]*len(id_list) # 각 유저별로 처리 결과 메일을 받은 횟수
    
    # 신고 정보 저장하기
    report_cnt = {id_:[] for id_ in id_list} # 신고된 유저의 ID : 신고한 유저의 ID들    
    for s in list(set(report)): # 중복 제거 (동일한 유저에 대한 신고 횟수는 1회로 처리)
        id1,id2 = s.split() # 신고한 유저의 ID, 신고된 유저의 ID
        report_cnt[id2].append(id1)
    
    # 신고 당한 이용자를 순서대로 확인
    for key in id_list:
        # k번 이상 신고된 유저인 경우
        if len(report_cnt[key]) >= k:
            # 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
            for id_ in report_cnt[key]:
                answer[id_list.index(id_)] += 1 # 메일 받는 횟수 증가
    return answer

print(solution(["muzi","frodo","apeach","neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)) # [2,1,1,0]
print(solution(["con","ryan"],["ryan con","ryan con","ryan con","ryan con"],3)) # [0,0]
# 튜플
# 2019 카카오 개발자 겨울 인턴십

def solution(s):
    answer = []
    visited = [0]*100001 # answer에 들어가있는지 여부 판단
    # 파싱하여 리스트로 저장하고 튜플의 길이 순으로 정렬
    tuples = sorted([list(map(int,tp.split(","))) for tp in s[2:len(s)-2].split("},{")], key=lambda x : len(x))
    for tp in tuples: # 튜플 탐색
        for num in tp: # 해당 튜플의 숫자 탐색
            if not visited[num]: # answer에 없는 숫자 찾아서 넣기
                visited[num] = 1
                answer.append(num)
                break
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2, 1, 3, 4]
print(solution("{{20,111},{111}}")) # [111, 20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3, 2, 4, 1]
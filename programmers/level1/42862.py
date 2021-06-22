# 체육복
# 탐욕법(Greedy)

# 도난 당한 idx번째 학생이 체육복을 빌릴 수 있는지 판단
def f(idx, lost, reserve, cnt): # cnt : 체육 수업을 들을 수 있는 학생 수
    global answer
    if idx == len(lost): # 마지막 학생인 경우 함수 종료
        if answer < cnt: answer = cnt # answer 갱신
        return
    for i in range(len(reserve)):
        # 여벌을 갖고 있는 학생(i)과 도난 당한 학생(idx)의 번호 차이가 1이며, 아직 여벌의 체육복을 빌려주지 않은 경우
        # = 체육복을 빌릴 수 있음
        if abs(reserve[i]-lost[idx]) == 1 and not visited[i]:
            visited[i] = 1
            f(idx+1, lost, reserve, cnt+1) # 체육 수업을 듣는 학생 수를 갱신
            visited[i] = 0
        # 체육복을 빌리지 못한 경우
        f(idx+1, lost, reserve, cnt)

def solution(n, lost, reserve):
    global answer, visited
    # 여벌 체육복을 가져왔으나 도난 당한 학생 처리
    # lost와 reserve 두 리스트 모두에 들어있는 번호 제거
    lost,reserve = list(set(lost)-set(reserve)),list(set(reserve)-set(lost))
    visited = [0]*len(reserve) # 여벌 체육복을 가져온 학생이 다른 학생에게 빌려주면 체크
    answer = n-len(lost) # 체육 수업을 들을 수 있는 학생 수 : 체육복을 도난 당하지 않은 학생 수로 초기화
    f(0, lost, reserve, n-len(lost))
    return answer

print(solution(5,[2,4],[1,3,5])) # 5
print(solution(5,[2,4],[3])) # 4
print(solution(3,[3],[1])) # 2
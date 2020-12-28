# 기능개발
# 스택/큐

from collections import deque

def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    q = deque([(99-progresses[i])//speeds[i]+1 for i in range(N)])
    while q:
        cur = q.popleft()
        cnt = 1 # 배포되는 기능의 개수
        for i in range(len(q)):
            tmp = q[0]
            if tmp > cur:
                cur = tmp
                break
            cnt += 1
            q.popleft()
        answer.append(cnt)
    return answer

print(solution([93,30,55], [1,30,5])) # [2,1]
print(solution([95,90,99,99,80,99], [1,1,1,1,1,1])) # [1,3,2]
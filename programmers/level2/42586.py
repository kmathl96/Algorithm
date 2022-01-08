# 기능개발
# 스택/큐

from collections import deque

def solution(progresses, speeds):
    answer = []
    N = len(progresses) # 작업의 개수
    
    # 작업을 완료하는 데 걸리는 기간
    q = deque([(99-progresses[i])//speeds[i]+1 for i in range(N)])
    
    while q:
        cur = q.popleft() # 배포할 기능
        cnt = 1 # 배포되는 기능의 개수
        
        for i in range(len(q)):
            tmp = q[0] # 다음 기능의 개발 완료 기간
            
            # 앞에 있는 기능보다 오래 걸리면 다음에 배포 => 종료
            if tmp > cur: break

            # 앞에 있는 기능과 같이 배포됨
            cnt += 1 # 배포 기능 개수 증가
            q.popleft() # 큐에서 제거

        answer.append(cnt) # 배포되는 기능의 개수 넣기
    return answer

print(solution([93,30,55], [1,30,5])) # [2,1]
print(solution([95,90,99,99,80,99], [1,1,1,1,1,1])) # [1,3,2]
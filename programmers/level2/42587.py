# 프린터
# 스택/큐

from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    idx = deque(range(len(priorities)))
    cnt = 0
    while True:
        if q[0] == max(q):
            q.popleft()
            cnt += 1
            if idx.popleft() == location:
                return cnt
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())

print(solution([2,1,3,2],2)) # 1
print(solution([1,1,9,1,1,1],0)) # 5
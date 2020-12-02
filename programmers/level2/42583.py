# 다리를 지나는 트럭
# 스택/큐

from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    trucks = deque(truck_weights)
    q = deque()
    flag = True # 트럭이 다리 위에 올랐는지 여부 판단
    while trucks or not flag:
        if flag: # 이전 트럭이 다리를 오른 경우 다음 트럭을 구함
            nxt = trucks.popleft()
            flag = False
        if sum([i[0] for i in q]) + nxt <= weight: # 트럭이 다리 위에 올라도 괜찮다면
            q.append((nxt,cnt)) # 다리 위에 올리고
            flag = True # 해당 트럭이 다리에 올랐으므로 다음에 오를 트럭 구해야 함
        cnt += 1
        # 현재 다리 위의 맨 앞 트럭이 다 건넜을 경우 제거
        if cnt >= q[0][1] + bridge_length:
            q.popleft()
    return cnt + bridge_length

print(solution(2,10,[7,4,5,6])) # 8
print(solution(100,100,[10])) # 101
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10])) # 110
print(solution(5,5,[2,2,2,2,1,1,1,1,1])) # 19
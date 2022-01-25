# A → B
# BFS

from collections import deque

A,B = map(int,input().split()) # A를 B로 바꾸기

# 연산의 최솟값을 구하기 위해 BFS를 사용
q = deque([(A,0)]) # 큐 : (현재 값, 연산 횟수)
answer = -1 # A를 B로 바꾸는 데 필요한 연산의 최솟값 : 만들 수 없는 경우에는 -1을 출력
while q:
    num,d = q.popleft()

    # B가 만들어진 경우, answer를 `연산횟수+1`로 변경하고 종료
    if num == B:
        answer = d+1
        break
    # B보다 큰 경우, 연산을 더 할 필요가 없으므로 넘어감
    elif num > B: continue

    # 1. `2를 곱한 수`를 큐에 넣음
    q.append((num*2,d+1))
    # 2. `1을 수의 가장 오른쪽에 추가한 수`를 큐에 넣음
    q.append((num*10+1,d+1))

print(answer)
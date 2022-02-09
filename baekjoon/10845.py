# 큐

from collections import deque
import sys
input = sys.stdin.readline

q = deque() # 큐
ans = [] # 출력할 결과 리스트
for _ in range(int(input())): # 입력된 명령의 수 만큼 반복
    cmd = input().split() # 명령
    # 정수 X를 큐에 넣는 연산
    if cmd[0] == 'push':
        q.append(cmd[1])
    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
    # 없는 경우에는 -1을 출력
    elif cmd[0] == 'pop':
        ans.append(q.popleft() if q else -1)
    # 큐에 들어있는 정수의 개수를 출력
    elif cmd[0] == 'size':
        ans.append(len(q))
    # 큐가 비어있으면 1, 아니면 0을 출력
    elif cmd[0] == 'empty':
        ans.append(0 if q else 1)
    # 큐의 가장 앞에 있는 정수(없는 경우에는 -1)를 출력
    elif cmd[0] == 'front':
        ans.append(q[0] if q else -1)
    # 큐의 가장 뒤에 있는 정수(없는 경우에는 -1)를 출력
    elif cmd[0] == 'back':
        ans.append(q[-1] if q else -1)

# 한 줄에 하나씩 결과 출력
for i in ans:
    print(i)
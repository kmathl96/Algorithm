# 덱

from collections import deque
import sys
input = sys.stdin.readline

ans = [] # 출력할 결과를 담을 리스트
dq = deque() # 덱
for _ in range(int(input())): # 주어지는 명령의 수(N) 만큼 반복
    cmd = input().split() # 명령
    
    # 정수 X를 덱의 앞에 넣기
    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])
    # 정수 X를 덱의 뒤에 넣기
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])
    # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력
    # 없는 경우에는 -1 출력
    elif cmd[0] == 'pop_front':
        ans.append(dq.popleft() if dq else -1)
    # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력
    # 없는 경우에는 -1 출력
    elif cmd[0] == 'pop_back':
        ans.append(dq.pop() if dq else -1)
    # 덱에 들어있는 정수의 개수 출력
    elif cmd[0] == 'size':
        ans.append(len(dq))
    # 덱이 비어있으면 1을, 아니면 0을 출력
    elif cmd[0] == 'empty':
        ans.append(0 if dq else 1)
    # 덱의 가장 앞에 있는 정수(없는 경우에는 -1)를 출력
    elif cmd[0] == 'front':
        ans.append(dq[0] if dq else -1)
    # 덱의 가장 뒤에 있는 정수(없는 경우에는 -1)를 출력
    elif cmd[0] == 'back':
        ans.append(dq[-1] if dq else -1)

# 한 줄에 하나씩 출력
for num in ans:
    print(num)
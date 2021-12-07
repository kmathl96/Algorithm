# 에디터
# 자료 구조, 스택

from collections import deque
import sys
input = sys.stdin.readline

# 1. 하나의 리스트로 풀기 => 시간 초과
# string = list(input())
# pos = len(string)
# for _ in range(int(input())):
#     cmd = input()
#     if cmd[0] == 'L' and pos != 0: pos -= 1
#     elif cmd[0] == 'D' and pos != len(string): pos += 1
#     elif cmd[0] == 'B' and pos != 0:
#         string.pop(pos-1)
#         pos -= 1
#     elif cmd[0] == 'P':
#         string.insert(pos,cmd[2])
#         pos += 1
# print(''.join(string))

# 2. 두 개의 큐로 풀기
# 커서의 위치를 기준으로 왼쪽 큐와 오른쪽 큐로 나눔
left_q,right_q = deque(list(input())[:-1]),deque()
for _ in range(int(input())):
    cmd = input() # 명령어

    # 커서를 왼쪽으로 한 칸 옮김
    # => 왼쪽 큐의 마지막 요소를 오른쪽 큐의 첫 자리에 넣기
    # 커서가 문장의 맨 앞이면 무시됨 => 왼쪽 큐에 요소가 있는지 확인
    if cmd[0] == 'L' and left_q:
        right_q.appendleft(left_q.pop())
    
    # 커서를 오른쪽으로 한 칸 옮김
    # => 오른쪽 큐의 첫 요소를 왼쪽 큐의 마지막 자리에 넣기
    # 커서가 문장의 맨 뒤이면 무시됨 => 오른쪽 큐에 요소가 있는지 확인
    elif cmd[0] == 'D' and right_q: left_q.append(right_q.popleft())
    
    # 커서 왼쪽에 있는 문자를 삭제함
    # => 왼쪽 큐의 마지막 요소 삭제
    # 커서가 문장의 맨 앞이면 무시됨 => 왼쪽 큐에 요소가 있는지 확인
    elif cmd[0] == 'B' and left_q: left_q.pop()
    
    # 문자를 커서 왼쪽에 추가함
    # => 왼쪽 큐에 넣기
    elif cmd[0] == 'P': left_q.append(cmd[2])

print(''.join(left_q)+''.join(right_q))

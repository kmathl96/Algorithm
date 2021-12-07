# 스택

import sys
input = sys.stdin.readline

st = [] # 스택
for _ in range(int(input())):
    cmd = input().split() # 명령
    if cmd[0] == 'push':
        st.append(cmd[1]) # 정수를 스택에 넣음
    elif cmd[0] == 'pop':
        # 스택에서 가장 위에 있는 정수를 빼고 그 수를 출력
        # 스택에 들어있는 정수가 없는 경우, -1 출력
        print(st.pop() if st else -1)
    elif cmd[0] == 'size':
        print(len(st)) # 스택에 들어있는 정수의 개수 출력
    elif cmd[0] == 'empty':
        # 스택이 비어있으면 1, 아니면 0 출력
        print(int(not st))
    else: # 'top'
        # 스택의 가장 위에 있는 정수 출력
        # 스택에 들어있는 정수가 없는 경우 -1 출력
        print(st[-1] if st else -1)
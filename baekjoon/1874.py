# 스택 수열
# 자료 구조, 스택

import sys
input = sys.stdin.readline

# 1~n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 수열 만들기
n = int(input())
nums = list(int(input()) for _ in range(n)) # 수열
st = [] # 스택
number = 1 # 스택에 넣을 수
answer = [] # 수열을 만들기 위해 필요한 연산 (push(+)/pop(-))

# 수열 순서대로 스택에서 꺼내기
for num in nums:
    # 해당 숫자까지 스택에 넣기
    while number <= num:
        st.append(number)
        number += 1
        answer.append('+') # (push)
    
    # 해당 숫자가 스택의 마지막 숫자와 같은 경우
    if st.pop() == num:
        answer.append('-') # (pop)
    else: # 다른 경우
        answer = ['NO'] # NO를 출력하도록 answer를 변경하고 종료
        break
for ans in answer: print(ans)
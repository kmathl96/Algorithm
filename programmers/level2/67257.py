# 수식 최대화
# 2020 카카오 인턴십

from collections import deque
from itertools import permutations

# 연산자에 따라 계산한 값을 반환
def cal(a,b,op):
    if op == '+': return a+b
    if op == '-': return a-b
    if op == '*': return a*b

def solution(expression):
    answer = 0 # 최대 연산 결과 값

    # 연산자와 수를 각 리스트에 순서대로 넣기
    ops,nums = [],[] # 연산자와 수를 넣을 리스트
    n_idx = 0 # 숫자의 첫 index값
    for i in range(len(expression)):
        s = expression[i] # 현재 처리할 문자
        if s in ('+','-','*'): # 연산자인 경우
            ops.append(s) # 연산자 넣기
            nums.append(int(expression[n_idx:i])) # 이전의 문자들은 숫자
            n_idx = i+1 # 다음 숫자의 첫 index값
    nums.append(int(expression[n_idx:])) # 마지막 숫자 넣기

    set_ops = set(ops) # 수식에 있는 연산자들 (중복 제거)
    cases = permutations(set_ops) # 연산자들로 우선순위 조합을 만듦

    # 각 우선순위 조합에 맞게 연산
    for case in cases:
        q_ops,q_nums = deque(ops),deque(nums) # deque에 연산자들, 숫자들을 각각 넣어서 연산자 q, 숫자 q를 만듦
        for i in range(len(set_ops)): # 우선순위대로 연산
            q_nums.append(q_nums.popleft()) # 맨 첫 숫자를 꺼내 넣기
            for _ in range(len(q_ops)): # 남아있는 연산자 만큼 연산
                # 숫자 q의 맨 마지막 숫자와 첫 숫자, 연산자 q의 첫 연산자
                num1,num2,op = q_nums.pop(),q_nums.popleft(),q_ops.popleft()
                # 해당 우선순위의 연산자인 경우
                if op == case[i]:
                    q_nums.append(cal(num1,num2,op)) # 연산하여 숫자 q에 넣기
                # 아닌 경우, 연산하지 않고 각 q에 넣음
                else:
                    q_nums.append(num1)
                    q_nums.append(num2)
                    q_ops.append(op)
        answer = max(answer,abs(q_nums[0])) # 연산 결과 값과 비교하여 더 큰 값으로 answer 갱신
    return answer

print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300
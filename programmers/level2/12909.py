# 올바른 괄호

def solution(s):
    st = []
    for i in s:
        if i=='(': # 열린 괄호는 스택에 넣기
            st.append(i)
        else: # 닫힌 괄호인 경우
            if not st or st.pop() == ')': # 스택이 비었거나 스택의 최상단이 닫힌 괄호일 경우 False 리턴
                return False
    if st: return False # 스택이 비어있지 않으면, 모두 닫히지 않은 것이므로 False 리턴
    return True

print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false
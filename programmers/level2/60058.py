# 괄호 변환
# 2020 KAKAO BLIND RECRUITMENT

def solution(p):
    if not p: return '' # 1. 빈 문자열인 경우, 빈 문자열 반환
    st = [] # 올바른지 판단하기 위한 변수
    cnt = 0 # 균형잡혀있는지 판단하기 위한 변수 (괄호에 따라 증감)
    for i in range(len(p)):
        u,v = p[:i+1],p[i+1:] # 2. 두 문자열로 분리
        if u[i]=='(':
            cnt += 1 # 열린 괄호는 +1
            st.append('(')
        else:
            cnt -= 1 # 닫힌 괄호는 -1
            if st and st[-1]=='(': # st 맨 위가 열린 괄호인 경우 올바름
                st.pop()
                # st이 비게 되면, 괄호의 짝이 모두 맞는 경우
                if not st: return u + solution(v) # 3. v에 대해 같은 과정 수행, 그 결과를 u에 붙인 후 반환
            else: st.append(')') # st에 닫힌 괄호 넣기
        if not cnt: # 열린/닫힌 괄호의 개수가 서로 같은 경우 (= 균형잡힌 괄호 문자열)
            # 4-1~3. '(' + v에 대해 같은 과정을 수행한 결과 + ')'
            # 4-4. u의 첫번째와 마지막을 제거(u[1:-1])한 문자열의 괄호 방향을 뒤집어서 붙임
            return '(' + solution(v) + ')' + ''.join(['(' if s==')' else ')' for s in u[1:-1]])

print(solution("(()())()")) # "(()())()"
print(solution(")(")) # "()"
print(solution("()))((()")) # "()(())()"
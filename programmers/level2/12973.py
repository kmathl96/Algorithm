# 짝지어 제거하기
# 2017 팁스타운

def solution(s):
    st = [s[0]] # 첫 문자는 바로 스택에 넣기
    for i in range(1,len(s)):
        if st and st[-1] == s[i]: # 스택 맨 위와 같은 문자인 경우
            st.pop() # 스택에서 해당 문자 제거
        else: st.append(s[i]) # 스택이 비어있거나 스택 맨 위와 다른 문자인 경우 스택에 넣기
    return 0 if st else 1 # 스택이 비어있으면 모든 문자가 제거된 것이므로 1 반환, 그렇지 않은 경우 0 반환

print(solution("baabaa")) # 1
print(solution("cdcd")) # 0
# 괄호 회전하기
# 월간 코드 챌린지 시즌2

dic = {'(':')', '{':'}','[':']'} # 특정 괄호의 짝이 맞는지 찾기 위함

def solution(s):
    answer = 0 # 올바른 괄호 문자열이 되게 하는 x의 개수
    N = len(s) # 문자열의 길이
    for x in range(N): # s를 x칸만큼 회전시킨 경우 (0 <= x <N)
        st = [] # 괄호가 올바르게 짝지어지는지 확인하기 위한 스택
        is_correct = 1 # 올바른지 여부
        for i in range(N): # s를 x칸 만큼 회전시킨 문자열이 올바른 괄호 문자열인지 확인
            substr = s[(x+i)%N] # s를 x칸 만큼 회전시킨 문자열의 (i+1)번째 괄호
            # 열린 괄호인 경우, st에 넣기
            if substr in dic.keys(): st.append(substr)
            # 닫힌 괄호인 경우
            else:
                # st의 마지막 괄호와 짝이 맞는 경우, st에서 해당 괄호 제거
                if st and dic[st[-1]] == substr: st.pop()
                # 짝이 맞지 않는 경우, 올바르지 않다고 갱신하고 종료
                else:
                    is_correct = 0 
                    break
        # st이 비어있고 올바른 경우, answer 갱신
        if not st and is_correct: answer += 1
    return answer

print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}")) # 0
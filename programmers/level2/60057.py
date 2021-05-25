# 문자열 압축
# 2020 KAKAO BLIND RECRUITMENT

def solution(s):
    N = len(s)
    answer = N
    for i in range(1,N//2+1): # 압축 단위 : 문자열 길이의 반이 최대
        temp_ans = N # 해당 압축 단위로 잘라 압축했을 때의 길이 (원래 문자열의 길이로 초기화)
        substr = s[:i] # 자른 문자열 초기화
        cnt = 1 # 문자열의 반복 횟수
        for idx in range(i,N,i): # 비교할 값의 첫 글자 index 값
            # 1. 다음 문자열과 같은 경우
            if substr == s[idx:idx+i]:
                temp_ans -= i # 압축 단위만큼 줄어듦
                cnt += 1 # 반복 횟수 증가
                if cnt in (2,10,100):
                    # 반복되지 않으면 문자열 앞에 숫자를 넣지 않고, 반복되면 숫자(2)를 넣으므로 자릿수 +1
                    # 반복 횟수가 10, 100이면 자릿수가 1 증가함
                    temp_ans += 1
            # 2. 다음 문자열과 다른 경우
            else:
                substr = s[idx:idx+i] # 탐색하기 위해 다음 문자열 저장
                cnt = 1 # 문자열 반복 횟수 초기화
        if answer > temp_ans: # 현재 답보다 작으면 갱신
            answer = temp_ans
    return answer

print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17

print(solution("aaaaaaaaaab")) # 4
print(solution("aababa")) # 5
print(solution("xxxxxxxxxxyyy")) # 5
print(solution("a")) # 1
print(solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")) # 4
print(solution("zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")) # 5
print(solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz")) # 5
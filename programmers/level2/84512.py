# 모음 사전

string = 'AEIOU' # 모음 알파벳

# 사전 만들기
dic = [''] # 사전
st = [('',0)] # 스택
while st:
    s,d = st.pop() # 문자열, 길이
    if d==5: continue # 사전에 수록된 단어의 최대 길이 = 5
    for i in string:
        st.append((s+i,d+1)) # 문자를 붙여서 스택에 넣기
        dic.append(s+i) # 사전에 넣기
dic.sort() # 정렬

def solution(word):
    return dic.index(word) # 사전에서 몇 번째 단어인지 반환

print(solution("AAAAE")) # 6
print(solution("AAAE")) # 10
print(solution("I")) # 1563
print(solution("EIO")) # 1189
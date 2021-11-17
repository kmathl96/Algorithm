# 압축
# 스택

# 압축된 부분 문자열 K(Q)를 풀기
st = [] # (문자열을 반복할 횟수(K), 이전 문자열의 길이)를 넣을 스택
length = 0 # 문자열의 길이
num = 0 # 문자열을 반복할 횟수(K)
for s in list(input()): # 문자를 순서대로
    if s == '(':
        st.append((num,length-1)) # K와 이전 문자열의 길이(문자열 길이에서 1(K의 길이)을 뺀 값)
        length = 0 # 문자열의 길이 초기화
    elif s == ')':
        n, pre_length = st.pop()
        length = pre_length + n*length # 문자열의 길이 = 이전 문자열의 길이 + 문자열(Q)를 n번 반복한 길이
    else: # 숫자인 경우
        length += 1 # 문자열의 길이 증가
        num = int(s) # 다음 문자가 '('인 경우 반복할 횟수(K)가 됨
print(length)
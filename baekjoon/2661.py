# 좋은수열
# 백트래킹

N = int(input()) # 수열의 길이
st = ['1'] # 스택
while st:
    num = st.pop() # 현재 수열

    # 길이가 N인 경우, 출력하고 종료
    if len(num)==N:
        print(num)
        break

    # 현재 수열의 뒤에 숫자 붙이기
    for i in '321': # 스택은 뒤에서부터 빼므로 큰 숫자부터 붙이기
        new = num+i # 새로운 수열

        # 좋은 수열인지 확인
        is_bad = 0 # 나쁜 수열 여부
        for l in range(1,len(new)//2+1): # 비교할 부분 수열의 길이
            # 두 부분 수열이 동일한 경우, 나쁜 수열이므로 확인 종료
            if new[-l:] == new[-2*l:-l]:
                is_bad = 1
                break
        
        # 나쁜 수열이 아닌 경우, 스택에 넣기
        if not is_bad:
            st.append(new)
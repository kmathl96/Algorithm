# 부등호
# 브루트포스, 백트래킹

k = int(input()) # 순서열의 크기
A = list(input().split()) # 부등호 기호가 나열된 순서열
max_ans,min_ans = '','' # 부등호 관계를 만족하는 최대 정수와 최소 정수
max_s,min_s = '9','0' # 최대/최소 정수를 만들 부분 문자열
max_num,min_num = 8,1 # 문자열에 붙일 수

# 부등호를 확인하며 최대/최소 정수 문자열 만들기
for s in A:
    # 다음 숫자가 더 커야 한다면,
    if s == '<':
        # 최대 정수를 만들 부분 문자열의 앞부분에 추가
        max_s = str(max_num)+max_s
        # 최소 정수의 뒤에 부분 문자열을 붙이고, 부분 문자열을 현재 숫자로 변경
        min_ans += min_s
        min_s = str(min_num)
    # 다음 숫자가 더 작아야 한다면,
    else:
        # 최대 정수의 뒤에 부분 문자열을 붙이고, 부분 문자열을 현재 숫자로 변경
        max_ans += max_s
        max_s = str(max_num)
        # 최소 정수를 만들 부분 문자열의 앞부분에 추가
        min_s = str(min_num)+min_s
    # 숫자 갱신
    max_num -= 1
    min_num += 1

# 각 부분 문자열을 붙여 최대/최소 정수를 출력
print(max_ans+max_s)
print(min_ans+min_s)
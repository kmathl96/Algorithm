# 전화번호 목록
# 문자열, 정렬

import sys
input = sys.stdin.readline

ans = [] # 각 테스트 케이스의 결과를 담을 리스트

# 입력된 테스트 케이스의 개수 만큼 반복
for _ in range(int(input())):
    n = int(input()) # 전화번호의 수
    numbers = sorted([input().rstrip() for _ in range(n)]) # 정렬된 전화번호 목록
    flag = 1 # 일관성이 있는지(1) 없는지(0) 여부

    # 전화번호 확인
    # 순서대로 정렬되어 있기 때문에 다음 전화번호의 접두어인지만 확인하면 됨
    for i in range(n-1):
        # 다음 전화번호의 접두어인 경우, 더 확인할 필요가 없으므로 종료
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            flag = 0 # 일관성 여부 변경
            break
    # 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO 저장
    ans.append('YES' if flag else 'NO')

for i in ans: print(i)
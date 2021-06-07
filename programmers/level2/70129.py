# 이진 변환 반복하기
# 월간 코드 챌린지 시즌1

def solution(s):
    cnt,removed = 0,0 # 이진 변환의 횟수, 변환 과정에서 제거된 모든 0의 개수 초기화
    while s!='1': # s가 "1"이 될 때까지 반복
        n = s.count('1') # 현재 문자열(s)의 1의 개수
        removed += s.count('0') # 제거된 0의 개수 갱신 (0의 개수를 더함)
        tmp = '' # 모든 0을 제거한 s의 길이(n)를 이진수로 만들어 저장
        while n:
            tmp = str(int(n)&1) + tmp
            n //= 2
        cnt += 1 # 이진 변환 횟수 증가
        s = tmp # 만들어진 이진수를 s에 저장
    return [cnt,removed]

print(solution("110010101001")) # [3,8]
print(solution("01110")) # [3,3]
print(solution("1111111")) # [4,1]
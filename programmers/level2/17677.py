# [1차] 뉴스 클러스터링
# 2018 KAKAO BLIND RECRUITMENT

import math

# 다중집합 구하기
def multiset(s):
    arr = []
    for i in range(len(s)-1):
        # A~Z에 속하는 문자인 경우만 다중집합의 원소가 될 수 있음
        if 65 <= ord(s[i]) <= 90 and 65 <= ord(s[i+1]) <= 90:
            arr.append(s[i:i+2])
    return arr

# 자카드 유사도 구하기
def J(A,B):
    if not len(A) and not len(B): return 1 # 두 다중집합이 공집합일 경우 1
    intersection,union = 0,0 # 합집합과 교집합의 개수 초기화
    for a in set(A):
        union += max(A.count(a), B.count(a)) # 합집합
        intersection += min(A.count(a), B.count(a)) # 교집합
    for b in set(B):
        if b not in A: # A에 있지 않은 B의 원소들의 개수를 합집합에 더함
            union += B.count(b)
    return intersection/union

def solution(str1, str2):
    str1,str2 = str1.upper(),str2.upper() # 대소문자 구분하지 않으므로 전부 대문자로 변경
    A,B = multiset(str1),multiset(str2) # 각 문자열의 다중집합 구하기
    return math.floor(J(A,B)*65536) # 자카드 유사도 구하기

print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12")) # 43690
print(solution("E=M*C^2", "e=m*c^2")) # 65536
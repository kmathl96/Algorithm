# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    return sorted(strings, key=lambda string: (string[n],string))

print(solution(['sun','bed','car'],1)) # ['car','bed','sun']
print(solution(['abce','abcd','cdx'],2)) # ['abcd','abce','cdx']
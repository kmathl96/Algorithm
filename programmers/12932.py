# 자연수 뒤집어 배열로 만들기

def solution(n):
    return list(map(int, list(str(n))))[::-1]

print(solution(12345)) # [5,4,3,2,1]
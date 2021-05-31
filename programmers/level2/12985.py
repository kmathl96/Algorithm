# 예상 대진표
# 2017 팁스타운

def solution(n,a,b):
    a,b = a-1,b-1 # 번호를 2로 나눈 몫이 같으면 만난 것으로 처리하기 위함
    for i in range(1,21): # 라운드 값
        a,b = a//2, b//2
        if a == b: return i

print(solution(8, 4, 7)) # 3
# 나머지가 1이 되는 수 찾기

def solution(n):
    # n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 구하기
    for x in range(1,n):
        # 나머지가 1인 경우 x를 반환하고 종료
        if n%x==1:
            return x

print(solution(10)) # 3
print(solution(12)) # 11
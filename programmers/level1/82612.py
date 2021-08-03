# 부족한 금액 계산하기
# 위클리 챌린지 1주차

def solution(price, money, count):
    # N번째 이용료 = N*price
    # 1~N번째 이용료의 합
    # = 1*price + 2*price + ... + N*price
    # = (1+2+...+N)*price
    # = (N*(N+1)//2)*price
    # 모자라는 금액과 0(금액이 부족하지 않는 경우) 중 큰 값 반환
    return max(price*count*(count+1)//2-money,0)

print(solution(3, 20, 4)) # 10
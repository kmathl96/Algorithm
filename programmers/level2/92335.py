# k진수에서 소수 개수 구하기

# 소수 판별
def is_prime(num):
    # 2 미만은 소수가 아님
    if num < 2: return 0
    for i in range(2,int(num**0.5)+1):
        if not num%i: return 0
    return 1

def solution(n, k):
    answer = 0 # 조건에 맞는 소수의 개수
    P = '' # 조건에 맞는 소수

    # k진법으로 바꾸면서 소수 계산해서 답 갱신
    while n:
        # 나머지가 있는 경우, 소수 갱신
        if n%k:
            P = str(n%k)+str(P)
        # 나머지가 없는 경우, 소수인지 판별
        elif P:
            answer += is_prime(int(P)) # 소수이면 1 증가
            P = '' # 소수 초기화
        n //= k
    
    # 마지막 숫자가 소수인지 판별하여 개수 계산
    if P: answer += is_prime(int(P))

    return answer

print(solution(437674,3)) # 3
print(solution(110011,10)) # 2
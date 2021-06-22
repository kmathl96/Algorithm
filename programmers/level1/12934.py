# 정수 제곱근 판별

def solution(n):
    x = int(n**0.5) # n의 제곱근에서 소수점 이하를 버린 값 (정수)
    # 그 수를 제곱한 값이 n과 같으면 그 다음 제곱수 반환, 아닌 경우 -1 반환
    return (x+1)**2 if x**2==n else -1

print(solution(121)) # 144
print(solution(3)) # -1
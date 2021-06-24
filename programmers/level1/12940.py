# 최대공약수와 최소공배수

# 최대공약수를 구하는 함수 (유클리드 호제법)
def f(a,b):
    # b가 0이 될 때까지 반복하여 최대공약수를 구함
    return f(b,a%b) if b else a

def solution(n, m):
    gcd = f(n,m) if n>m else f(m,n) # 두 수 중 큰 수를 첫 인자로 넣음
    return [gcd,n*m//gcd] # 최소공배수는 두 수를 곱한 것을 최대공약수로 나눈 값

print(solution(3, 12)) # [3,12]
print(solution(2, 5)) # [1,10]
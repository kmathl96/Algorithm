# 멀쩡한 사각형
# Summer/Winter Coding(2019)

# 최대공약수를 구하는 함수 (유클리드 호제법)
def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b) if a > b else gcd(a,b%a)

def solution(w,h):
    # w,h를 최대공약수로 나눈 값을 w',h'라고 하면,
    # w = w'*gcd(w,h), h = h'*gcd(w,h)
    # w'*h' 직사각형에서 대각선이 지나는 칸의 개수는 (w'-1)+(h'-1)+1 = w'+h'-1
    # w*h 직사각형에서 대각선이 지나는 칸의 개수는 (w'+h'-1)*gcd(w,h) = w+h-gcd(w,h)
    return w*h - (w+h-gcd(w,h)) # 전체 개수에서 대각선이 지나는 칸의 개수를 뺌

print(solution(8, 12)) # 80
print(solution(3, 3))
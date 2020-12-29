# 2609. 최대공약수와 최소공배수

def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

a,b = map(int, input().split())
if a > b: ans = gcd(a,b)
else: ans = gcd(b,a)

print(ans)
print(a*b//ans)
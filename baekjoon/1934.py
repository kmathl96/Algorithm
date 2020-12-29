# 최소공배수

def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

for i in range(int(input())):
    a,b = map(int, input().split())
    print(a*b//gcd(a,b))
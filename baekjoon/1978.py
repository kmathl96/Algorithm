# 소수 찾기

int(input())
arr = list(map(int,input().split()))
ans = 0
for a in arr:
    if a < 2: continue
    is_prime = True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            is_prime = False
            break
    if is_prime: ans += 1
print(ans)
# GCD 합

from itertools import combinations

def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    ans = 0
    for a,b in list(combinations(nums,2)):
        ans += gcd(a,b)
    print(ans)
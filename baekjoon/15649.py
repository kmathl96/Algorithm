# N과 M (1)
# 브루트 포스

from itertools import permutations

N,M = map(int,input().split())
for a in list(permutations(range(1,N+1),M)):
    print(*a)
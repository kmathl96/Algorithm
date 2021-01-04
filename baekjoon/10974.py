# 모든 순열
# SW 역량 테스트 준비 - 기초
# 브루트 포스

from itertools import permutations

N = int(input())
for p in permutations(range(1,N+1),N):
    print(*p)
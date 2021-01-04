# 암호 만들기
# 브루트 포스

from itertools import combinations

L,C = map(int,input().split())
arr = sorted(list(input().split())) # 정렬
cases = list(combinations(arr,L)) # 조합
for case in cases:
    cnt = 0 # 모음 개수 (자음 개수 = L-cnt)
    for i in case:
        if i in 'aeiou': cnt += 1
        if cnt > L-2: break # 자음 2개 조건을 충족시키지 못함
    if 0 < cnt < L-1: print("".join(case))
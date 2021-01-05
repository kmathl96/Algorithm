# 집합
# 브루트 포스
# input()으로 입력 받으면 시간 초과 => import sys => sys.stdin.readline()으로 입력 받기
# set의 remove는 해당 원소가 set에 존재하지 않을 경우 에러 => discard 사용

import sys

M = int(input())
S = set() # add, remove 처리하기 용이하도록 set 사용
for _ in range(M):
    tmp = sys.stdin.readline().split()
    op = tmp[0]
    if len(tmp)==1:
        if op=='all': S = set(range(1,21))
        else: S = set()
        continue
    x = int(tmp[1])
    if op=='add': S.add(x)
    elif op=='remove': S.discard(x) # 존재하면 제거 (존재하지 않아도 에러가 발생하지 않음)
    elif op=='check': print(1 if x in S else 0)
    elif op=='toggle':
        if x not in S: S.add(x)
        else: S.remove(x)
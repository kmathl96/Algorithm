# 수 정렬하기 2
# 정렬

import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수

# N개의 수를 오름차순 정렬한 뒤 순서대로 출력
for n in sorted([int(input()) for _ in range(N)]):
    print(n)
# 듣보잡
# 자료 구조, 문자열, 정렬

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 듣도 못한 사람의 수, 보도 못한 사람의 수

# 듣도 못한 사람의 이름과 보도 못한 사람의 이름의 교집합을 구해서 오름차순 정렬하기
names = sorted({input() for _ in range(N)}&{input() for _ in range(M)})

print(len(names)) # 듣보잡의 수
print(''.join(names)) # 명단
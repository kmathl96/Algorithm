# 저울
# 플로이드-와샬

import sys
input = sys.stdin.readline

N = int(input()) # 물건의 개수
M = int(input()) # 미리 측정된 물건 쌍의 개수

# d[i][j] = i가 j보다 무거움 => 무게 비교 결과를 알 수 있음
d = [[0]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split()) # a 무게 > b 무게
    d[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        # i와 k의 무게를 비교할 수 없으면 넘어감
        if not d[i][k]: continue
        for j in range(N):
            # i가 k보다 무겁고 k가 j보다 무거움 => i가 j보다 무거움
            if not d[i][j] and d[k][j]:
                d[i][j] = 1

# 각 물건에 대해서 그 물건과의 비교 결과를 알 수 없는 물건의 개수를 출력
# => (전체 물건-해당 물건)(=N-1)에서 비교 결과를 알 수 있는 물건의 개수를 뺀 값
# => 각 물건보다 가벼운 물건들의 개수(=sum(row))와 무거운 물건들의 개수(=sum(col))의 합
for row,col in zip(d,zip(*d)):
    print(N-1-sum(row)-sum(col))
# 케빈 베이컨의 6단계 법칙
# 플로이드-와샬

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 유저의 수, 친구 관계의 수

# d[i][j] = i와 j가 최소 몇 단계 만에 이어질 수 있는지
d = [[float('INF')]*N for _ in range(N)]
for _ in range(M):
    A,B = map(int,input().split()) # 친구 관계
    d[A-1][B-1] = 1
    d[B-1][A-1] = 1

# 케빈 베이컨 게임 하기
for k in range(N):
    d[k][k] = 0 # 본인은 0
    for i in range(N):
        for j in range(N):
            # k를 통하는 단계와 비교하여 더 작은 값으로 저장
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])

# 케빈 베이컨 게임을 했을때 나오는 단계의 총 합이 가장 적은 사람 구하기
sums = [sum(row) for row in d] # 각각의 총합
print(sums.index(min(sums))+1) # 최솟값의 인덱스 값
# 키 순서
# 플로이드-와샬

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 학생들의 수, 두 학생 키를 비교한 횟수
inf = float('INF')
d = [[inf]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split()) # 두 학생의 키
    d[a-1][b-1] = 1 # a가 b보다 작음

# 플로이드-와샬
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])

ans = 0 # 자신의 키가 몇 번째인지 알 수 있는 학생의 수
for i in range(N):
    cnt = 0 # 본인과 키 우열을 가릴 수 있는 학생의 수
    for j in range(N):
        # 본인보다 키가 크거나 작은 경우, 우열을 가릴 수 있음
        if d[i][j] != inf or  d[j][i] != inf:
            cnt += 1
    
    # (N-1)명과 우열을 가릴 수 있다면 본인의 키 순서를 알 수 있음
    if cnt==N-1:
        ans += 1
print(ans)
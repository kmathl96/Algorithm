# 키 순서
# 플로이드-와샬

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 학생들의 수, 두 학생 키를 비교한 횟수
d = [[0]*N for _ in range(N)] # 두 학생이 연결되어 있는지 여부
for _ in range(M):
    a,b = map(int,input().split()) # 두 학생의 키
    d[a-1][b-1] = 1 # a가 b보다 작음

# 플로이드-와샬
for k in range(N):
    # i-k, k-j가 연결되어 있다면, i-j도 연결되어 있는 것임
    for i in range(N):
        if not d[i][k]: continue # i-k가 연결되어 있지 않으면 넘어감
        for j in range(N):
            # i-j가 아직 연결되어 있지 않고 i-k, k-j가 연결되어 있는 경우
            if not d[i][j] and d[k][j]:
                d[i][j] = 1 # 연결 여부 체크

# 연결되어있는 학생의 수를 계산
# 1. i행에 연결 표시 된 학생은 i 학생보다 키가 작고
# 2. i열에 연결 표시 된 학생은 i 학생보다 키가 큼
# => 행과 열에 (N-1)명과 연결되어 있으면, 자신의 키가 몇 번째인지 알 수 있음
# => (N-1)명과 연결되어 있는 학생의 수 출력
print([sum(row)+sum(col) for row,col in zip(d,zip(*d))].count(N-1))
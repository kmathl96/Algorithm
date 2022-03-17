# 파도반 수열
# DP

import sys
input = sys.stdin.readline

# 파도반 수열 구하기
# N의 최댓값이 100이므로 100개까지 구하기
P = [0]*101 # 나선에 있는 정삼각형의 변의 길이
P[1],P[2],P[3],P[4] = 1,1,1,2
for i in range(5,101):
    P[i] = P[i-1]+P[i-5] # 1개 전 삼각형과 5개 전 삼각형과 변을 공유함

T = int(input()) # 테스트 케이스의 개수
for _ in range(T):
    N = int(input())
    print(P[N]) # 파도반 수열 P(N) 출력
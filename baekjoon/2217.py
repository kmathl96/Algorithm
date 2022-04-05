# 로프
# 수학, 그리디, 정렬

import sys
input = sys.stdin.readline

N = int(input()) # 로프의 개수

# 각 로프가 버틸 수 있는 최대 중량을 오름차순 정렬하여 저장
w = sorted([int(input()) for _ in range(N)])

# k개의 로프를 사용하는 경우, 그 중 최소 중량의 k배 만큼 들 수 있음 
# => i번째부터 마지막 로프까지 사용하는 경우, w[i]*(N-i)만큼 들 수 있음
# => 그 중 최댓값 출력
print(max(w[i]*(N-i) for i in range(N)))
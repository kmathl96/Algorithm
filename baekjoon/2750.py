# 수 정렬하기
# 구현, 정렬

import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수
nums = sorted(int(input()) for _ in range(N)) # N개의 수를 오름차순으로 정렬하여 저장

# 결과를 한 줄에 하나씩 출력
for num in nums:
    print(num)
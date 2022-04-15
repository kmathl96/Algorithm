# 수 정렬하기 3
# 정렬

import sys
input = sys.stdin.readline

def sol():
    N = int(input()) # 수의 개수

    # 각 정수의 입력된 횟수 저장
    cnt = [0]*10001
    for _ in range(N):
        cnt[int(input())] += 1
    
    # 각 정수의 개수만큼 정수 출력
    for k in range(1,10001):
        for i in range(cnt[k]):
            print(k)

sol()
# 회의실 배정
# 그리디, 정렬

import sys
input = sys.stdin.readline

N = int(input()) # 회의의 수
cnt = 0 # 최대 사용할 수 있는 회의의 최대 개수

# 회의 정보 저장
# 끝나는 시간과 시작 시간을 기준으로 오름차순 정렬
meeting = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x: (x[1],x[0]))

# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾기
time = 0 # 가장 최근에 회의가 끝난 시간
for s,e in meeting: # 시작 시간, 끝나는 시간
    # 이전 회의가 종료된 시간보다 시작 시간이 늦는 경우, 회의 진행
    if time <= s:
        time = e # 해당 회의가 끝난 시간으로 변경
        cnt += 1
print(cnt)
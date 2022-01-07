# 종이 조각
# 브루트포스, 비트마스킹

N,M = map(int,input().split()) # 종이 조각의 세로 크기와 가로 크기
paper = [list(map(int,list(input()))) for _ in range(N)] # 종이 조각의 각 칸에 적힌 수
ans = 0 # 잘린 종이 조각의 합 중 최댓값

# 각 칸은 가로 조각(0)이 되거나 세로 조각(1)이 되는 2가지 상태로 나뉨
# => 비트로 계산 : 비트의 오른쪽 숫자부터 순서대로 칸에 매핑됨
# ex) 2*3 종이 조각의 100101의 경우
#     | 1 | 0 | 1 |
#     |-------|   |
#     | 0   0 | 1 |
for case in range(1<<(N*M)):
    total = 0 # 종이 조각의 총합

    # 가로 종이 조각의 합
    for r in range(N):
        sub = 0 # 가로 종이 조각의 합
        for c in range(M):
            idx = r*M + c # 현재 경우의 비트(case)에서의 해당 칸의 위치

            # 해당 칸의 비트 확인
            # 현재 경우의 비트(case)와 해당 칸의 위치가 1인 비트(1<<idx)를 & 연산
            # => 0이면 현재 칸은 1이 아니고 가로 종이 조각을 구성하며, 1이면 세로 종이 조각임
            if case&(1<<idx): # 세로 조각인 경우
                total += sub # 지금까지의 가로 종이 조각의 합을 총합에 더함
                sub = 0 # 가로 종이 조각의 합 초기화
            else: # 가로 조각인 경우
                # 해당 칸이 현재 가로 종이 조각과 이어지므로, 해당 칸의 숫자를 더함
                sub = sub*10 + paper[r][c] # 가로 종이 조각의 합 갱신
        total += sub # 총합에 가로 종이 조각의 합을 더함
    
    # 세로 종이 조각의 합
    for c in range(M):
        sub = 0
        for r in range(N):
            idx = r*M + c
            if case&(1<<idx): # 현재 세로 종이 조각과 이어지는 경우
                sub = sub*10 + paper[r][c]
            else: # 가로 종이 조각인 경우
                total += sub
                sub = 0
        total += sub
    
    # 모든 종이 조각들의 합이 ans보다 큰 경우 변경
    if ans < total: ans = total
print(ans)
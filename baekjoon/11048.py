# 이동하기
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 미로의 크기

# 미로의 각 방에 놓인 사탕의 개수
# 해당 방으로 가져올 수 있는 사탕의 최대 개수를 저장
# 위와 왼쪽에 0을 한줄씩 추가하여, 이후에 계산하기 쉽도록 함
maze = [[0]*(M+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]

for r in range(1,N+1):
    for c in range(1,M+1):
        # 해당 방으로 이동할 수 있는 방들((r-1,c-1),(r-1,c),(r,c-1)) 중
        # 가장 많은 사탕의 개수를 더함
        maze[r][c] += max(maze[r-1][c-1],maze[r-1][c],maze[r][c-1])
print(maze[N][M]) # 마지막 방의 사탕 개수
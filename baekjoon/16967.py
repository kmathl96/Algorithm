# 배열 복원하기
# 구현

import sys
input = sys.stdin.readline

# 배열 B는 배열 A와 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을 겹쳐 만듦
# 배열 A의 크기 = H*W => 배열 B의 크기 = (H+X)*(W+Y)
H,W,X,Y = map(int,input().split()) # 배열 A의 크기와 두 정수
B = [list(map(int,input().split())) for _ in range(H+X)] # 배열 B의 원소

# 겹친 부분은 겹쳐진 수를 빼서 원래 A값으로 복원하기
for r in range(X,H):
    for c in range(Y,W):
        B[r][c] -= B[r-X][c-Y] # B(r-X,c-Y)의 수가 더해져있으므로 빼기

# H*W 범위의 B 원소들 출력
for row in B[:H]:
    print(*row[:W])
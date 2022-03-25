# 2차원 배열의 합
# 구현, 누적 합

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # 배열의 크기
arr = [[0]*(M+1)]+[[0]+list(map(int,input().split())) for _ in range(N)] # 배열

# 누적합 저장
# arr[i][j] = (0,0)~(i,j)의 합
for r in range(1,N+1):
    for c in range(1,M+1):
        arr[r][c] += arr[r-1][c]+arr[r][c-1]-arr[r-1][c-1]

K = int(input()) # 합을 구할 부분의 개수
ans = [] # 부분 합을 담을 리스트
for _ in range(K):
    i,j,x,y = map(int,input().split()) # 네 개의 정수 : (i,j)~(x,y)의 합 구하기
    # (0,0)~(x,y)의 합에서
    # (0,0)~(i-1,y),(0,0)~(x,j-1)의 합을 빼고
    # (0,0)~(i-1,j-1)의 합을 더한 값(뺄 때 중복되는 부분이므로 다시 더해야 함)과 같음
    ans.append(str(arr[x][y]-arr[i-1][y]-arr[x][j-1]+arr[i-1][j-1]))

print('\n'.join(ans))
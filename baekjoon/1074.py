# Z
# 분할 정복, 재귀

# (2^N * 2^N) 크기의 배열을 Z모양으로 탐색하여
# r행 c열을 몇 번째로 방문하는지 찾기
N,r,c = map(int,input().split())
ans = 0 # r행 c열을 방문한 순서
dirs = [(0,0),(0,1),(1,0),(1,1)] # Z모양으로 탐색하기 위한 방향 배열
num = 2**(N-1) # 4등분할 부분 배열의 크기
x,y = 0,0 # (r,c)가 속하는 부분 배열의 왼쪽 상단의 인덱스 값

# 배열을 4등분하는 것을 반복
for _ in range(N):
    # 4등분한 부분 배열 중, (r,c)가 속하는 부분 배열 찾기
    for i in range(4):
        dx,dy = dirs[i]
        nx,ny = x+dx*num,y+dy*num # 부분 배열의 왼쪽 상단 인덱스 값
        
        # (r,c)가 해당 부분 배열에 속하는 경우
        if nx<=r<nx+num and ny<=c<ny+num:
            x,y = nx,ny # 갱신
            ans += num*num*i # 이전 부분 배열들의 크기만큼 더하기
            break
    num //= 2 # 부분 배열의 크기가 절반으로 감소
print(ans)